from flask import request, jsonify, redirect, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from .. import db
from ..models import Link, Click, LinkDailyStats, Domain
from . import api
from datetime import datetime, timedelta
import validators
from urllib.parse import urlparse

@api.route('/links', methods=['POST'])
@jwt_required()
def create_link():
    """Create a new shortened URL"""
    current_user_id = int(get_jwt_identity())
    data = request.get_json()
    
    # Validate required fields
    if not data or 'long_url' not in data:
        return jsonify({"error": "Missing required field: long_url"}), 400
    
    # Validate URL format
    if not validators.url(data['long_url']):
        return jsonify({"error": "Invalid URL format"}), 400
    
    try:
        # Check if domain belongs to user if provided
        domain = None
        if 'domain_id' in data and data['domain_id']:
            domain = Domain.query.filter_by(
                domain_id=data['domain_id'], 
                user_id=current_user_id
            ).first()
            
            if not domain:
                return jsonify({"error": "Domain not found or access denied"}), 404
        
        # Set expiration date if provided
        expiration_date = None
        if 'expiration_days' in data and data['expiration_days']:
            expiration_date = datetime.utcnow() + timedelta(days=data['expiration_days'])
        
        # Create the link
        link = Link(
            long_url=data['long_url'],
            user_id=current_user_id,
            domain_id=domain.domain_id if domain else None,
            expiration_date=expiration_date,
            is_dynamic=data.get('is_dynamic', False)
        )
        
        db.session.add(link)
        db.session.flush()  # Get the link ID
        
        # If custom slug is provided, use it
        if 'custom_slug' in data and data['custom_slug']:
            # Check if slug is available
            existing = Link.query.filter_by(short_url_slug=data['custom_slug']).first()
            if existing:
                return jsonify({"error": "Custom slug already in use"}), 400
            link.short_url_slug = data['custom_slug']
        
        db.session.commit()
        
        return jsonify({
            "message": "Link created successfully",
            "link": link.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@api.route('/links', methods=['GET'])
@jwt_required()
def get_user_links():
    """Get all links for the current user"""
    current_user_id = int(get_jwt_identity())
    
    # Pagination
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Filtering
    query = Link.query.filter_by(user_id=current_user_id)
    
    # Search by long URL or slug
    search = request.args.get('search')
    if search:
        query = query.filter(
            (Link.long_url.ilike(f'%{search}%')) |
            (Link.short_url_slug.ilike(f'%{search}%'))
        )
    
    # Sorting
    sort_by = request.args.get('sort_by', 'creation_date')
    sort_order = request.args.get('sort_order', 'desc')
    
    if hasattr(Link, sort_by):
        column = getattr(Link, sort_by)
        if sort_order.lower() == 'desc':
            column = column.desc()
        query = query.order_by(column)
    
    # Execute query with pagination
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    links = pagination.items
    
    return jsonify({
        'links': [link.to_dict() for link in links],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    }), 200

@api.route('/links/<string:slug>', methods=['GET'])
@jwt_required()
def get_link(slug):
    """Get a specific link by slug"""
    current_user_id = int(get_jwt_identity())
    
    link = Link.query.filter_by(short_url_slug=slug).first()
    
    if not link:
        return jsonify({"error": "Link not found"}), 404
    
    # Check if the link belongs to the current user
    if link.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403
    
    return jsonify(link.to_dict()), 200

@api.route('/links/<string:slug>', methods=['PUT'])
@jwt_required()
def update_link(slug):
    """Update a link"""
    current_user_id = int(get_jwt_identity())
    data = request.get_json()
    
    link = Link.query.filter_by(short_url_slug=slug).first()
    
    if not link:
        return jsonify({"error": "Link not found"}), 404
    
    if link.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403
    
    try:
        # Update fields if provided
        if 'long_url' in data:
            if not validators.url(data['long_url']):
                return jsonify({"error": "Invalid URL format"}), 400
            link.long_url = data['long_url']
        
        if 'domain_id' in data:
            if data['domain_id'] is not None:
                domain = Domain.query.filter_by(
                    domain_id=data['domain_id'], 
                    user_id=current_user_id
                ).first()
                
                if not domain:
                    return jsonify({"error": "Domain not found or access denied"}), 404
                
                link.domain_id = domain.domain_id
            else:
                link.domain_id = None
        
        if 'expiration_days' in data:
            if data['expiration_days'] is None:
                link.expiration_date = None
            else:
                link.expiration_date = datetime.utcnow() + timedelta(days=data['expiration_days'])
        
        if 'is_dynamic' in data:
            link.is_dynamic = bool(data['is_dynamic'])
        
        db.session.commit()
        
        return jsonify({
            "message": "Link updated successfully",
            "link": link.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@api.route('/links/<string:slug>', methods=['DELETE'])
@jwt_required()
def delete_link(slug):
    """Delete a link"""
    current_user_id = int(get_jwt_identity())
    
    link = Link.query.filter_by(short_url_slug=slug).first()
    
    if not link:
        return jsonify({"error": "Link not found"}), 404
    
    if link.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403
    
    try:
        db.session.delete(link)
        db.session.commit()
        return jsonify({"message": "Link deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# NOTE: Redirect route is handled at root level in app/__init__.py
# This ensures cleaner URLs for QR codes (e.g., conlk.zen-apps.com/abc123)
# The root-level route at /<slug> takes precedence over API routes
