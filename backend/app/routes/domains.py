from flask import request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from .. import db
from ..models import Domain, Link
from . import api
import dns.resolver
from urllib.parse import urlparse

@api.route('/domains', methods=['POST'])
@jwt_required()
def add_domain():
    """Add a new custom domain"""
    current_user_id = int(get_jwt_identity())
    data = request.get_json()
    
    if not data or 'domain_name' not in data:
        return jsonify({"error": "Missing required field: domain_name"}), 400
    
    # Basic domain format validation
    domain_name = data['domain_name'].lower().strip()
    if not domain_name or '.' not in domain_name:
        return jsonify({"error": "Invalid domain format"}), 400
    
    # Check if domain is already registered
    existing_domain = Domain.query.filter_by(domain_name=domain_name).first()
    if existing_domain:
        return jsonify({"error": "Domain already registered"}), 400
    
    try:
        # In a production environment, you would verify domain ownership here
        # This is a simplified version that just checks DNS resolution
        try:
            dns.resolver.resolve(domain_name, 'A')
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers):
            return jsonify({"error": "Could not verify domain. Please make sure it's properly configured."}), 400
        
        # Create the domain
        domain = Domain(
            domain_name=domain_name,
            user_id=current_user_id,
            status='Pending'  # Would be 'Active' after verification in a real app
        )
        
        db.session.add(domain)
        db.session.commit()
        
        return jsonify({
            "message": "Domain added successfully. Please complete verification.",
            "domain": domain.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error adding domain: {str(e)}")
        return jsonify({"error": "An error occurred while adding the domain"}), 500

@api.route('/domains', methods=['GET'])
@jwt_required()
def get_user_domains():
    """Get all domains for the current user"""
    current_user_id = int(get_jwt_identity())
    
    domains = Domain.query.filter_by(user_id=current_user_id).all()
    
    return jsonify({
        'domains': [domain.to_dict() for domain in domains]
    }), 200

@api.route('/domains/<int:domain_id>', methods=['GET'])
@jwt_required()
def get_domain(domain_id):
    """Get a specific domain by ID"""
    current_user_id = int(get_jwt_identity())
    
    domain = Domain.query.get(domain_id)
    
    if not domain:
        return jsonify({"error": "Domain not found"}), 404
    
    if domain.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403
    
    return jsonify(domain.to_dict()), 200

@api.route('/domains/<int:domain_id>', methods=['PUT'])
@jwt_required()
def update_domain(domain_id):
    """Update domain information"""
    current_user_id = int(get_jwt_identity())
    data = request.get_json()
    
    domain = Domain.query.get(domain_id)
    
    if not domain:
        return jsonify({"error": "Domain not found"}), 404
    
    if domain.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403
    
    try:
        # In a real app, you might allow updating status after verification
        # For now, we'll just allow updating the status to 'Active' for testing
        if 'status' in data and data['status'] in ['Active', 'Pending', 'Suspended']:
            domain.status = data['status']
        
        db.session.commit()
        
        return jsonify({
            "message": "Domain updated successfully",
            "domain": domain.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error updating domain: {str(e)}")
        return jsonify({"error": "An error occurred while updating the domain"}), 500

@api.route('/domains/<int:domain_id>', methods=['DELETE'])
@jwt_required()
def delete_domain(domain_id):
    """Delete a domain"""
    current_user_id = int(get_jwt_identity())
    
    domain = Domain.query.get(domain_id)
    
    if not domain:
        return jsonify({"error": "Domain not found"}), 404
    
    if domain.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403
    
    # Check if the domain is being used by any links
    links_using_domain = Link.query.filter_by(domain_id=domain_id).count()
    if links_using_domain > 0:
        return jsonify({
            "error": f"Cannot delete domain: {links_using_domain} links are using this domain"
        }), 400
    
    try:
        db.session.delete(domain)
        db.session.commit()
        
        return jsonify({"message": "Domain deleted successfully"}), 200
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error deleting domain: {str(e)}")
        return jsonify({"error": "An error occurred while deleting the domain"}), 500

@api.route('/domains/verify', methods=['POST'])
@jwt_required()
def verify_domain():
    """Verify domain ownership"""
    current_user_id = int(get_jwt_identity())
    data = request.get_json()
    
    if not data or 'domain_id' not in data:
        return jsonify({"error": "Missing required field: domain_id"}), 400
    
    domain = Domain.query.get(data['domain_id'])
    
    if not domain:
        return jsonify({"error": "Domain not found"}), 404
    
    if domain.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403
    
    # In a real app, you would check for a specific DNS record or file on the domain
    # This is a simplified version that just checks DNS resolution
    try:
        dns.resolver.resolve(domain.domain_name, 'TXT')
        # If we get here, the domain resolves
        domain.status = 'Active'
        db.session.commit()
        
        return jsonify({
            "message": "Domain verified successfully",
            "domain": domain.to_dict()
        }), 200
        
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers):
        return jsonify({"error": "Could not verify domain ownership. Please add the required DNS record."}), 400
    except Exception as e:
        current_app.logger.error(f"Error verifying domain: {str(e)}")
        return jsonify({"error": "An error occurred while verifying the domain"}), 500
