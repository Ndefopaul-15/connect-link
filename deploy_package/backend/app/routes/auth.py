from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db, bcrypt
from ..models import User, PointsLedger
from . import api
from datetime import timedelta, datetime
import secrets

@api.route('/auth/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.get_json()
    
    # Validate input
    if not all(k in data for k in ['email', 'password']):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Check if user already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400
    
    try:
        # Create new user
        user = User(
            email=data['email'],
            password=data['password']
        )
        
        # Add to database
        db.session.add(user)
        db.session.flush()  # Get the user ID
        
        # Award points for signup
        PointsLedger.create_transaction(
            user=user,
            points_amount=100,  # Example: 100 points for signing up
            transaction_type='signup_bonus'
        )
        
        # Create access token
        access_token = create_access_token(
            identity=str(user.user_id),
            expires_delta=timedelta(days=7)
        )
        
        db.session.commit()
        
        return jsonify({
            "message": "User registered successfully",
            "access_token": access_token,
            "user": user.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@api.route('/auth/login', methods=['POST'])
def login():
    """User login"""
    data = request.get_json()
    
    # Validate input
    if not all(k in data for k in ['email', 'password']):
        return jsonify({"error": "Missing email or password"}), 400
    
    # Find user
    user = User.query.filter_by(email=data['email']).first()
    
    # Check if user exists and password is correct
    if not user or not user.check_password(data['password']):
        return jsonify({"error": "Invalid email or password"}), 401
    
    # Create access token
    access_token = create_access_token(
        identity=str(user.user_id),
        expires_delta=timedelta(days=7)
    )
    
    return jsonify({
        "access_token": access_token,
        "user": user.to_dict()
    }), 200

@api.route('/auth/me', methods=['GET'])
@jwt_required()
def get_current_user():
    """Get current user's profile"""
    current_user_id = int(get_jwt_identity())
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
        
    return jsonify(user.to_dict()), 200

@api.route('/auth/change-password', methods=['PUT'])
@jwt_required()
def change_password():
    """Change user's password"""
    current_user_id = int(get_jwt_identity())
    data = request.get_json()
    
    if not all(k in data for k in ['current_password', 'new_password']):
        return jsonify({"error": "Missing required fields"}), 400
    
    user = User.query.get(current_user_id)
    
    if not user or not user.check_password(data['current_password']):
        return jsonify({"error": "Invalid current password"}), 401
    
    try:
        user.password = bcrypt.generate_password_hash(data['new_password']).decode('utf-8')
        db.session.commit()
        return jsonify({"message": "Password updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@api.route('/auth/forgot-password', methods=['POST'])
def forgot_password():
    """Request password reset"""
    data = request.get_json()
    
    if 'email' not in data:
        return jsonify({"error": "Email is required"}), 400
    
    user = User.query.filter_by(email=data['email']).first()
    
    # Always return success to prevent email enumeration
    if not user:
        return jsonify({"message": "If the email exists, a reset link has been sent"}), 200
    
    try:
        # Generate reset token
        reset_token = secrets.token_urlsafe(32)
        user.reset_token = reset_token
        user.reset_token_expiry = datetime.utcnow() + timedelta(hours=1)
        db.session.commit()
        
        # TODO: Send email with reset link
        # For now, we'll just return the token (in production, send via email)
        reset_url = f"http://localhost:5175/reset-password?token={reset_token}"
        
        # In production, you would send an email here
        # send_email(user.email, "Password Reset", f"Click here to reset: {reset_url}")
        
        print(f"Password reset link for {user.email}: {reset_url}")
        
        return jsonify({
            "message": "If the email exists, a reset link has been sent",
            "reset_url": reset_url  # Remove this in production
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to process request"}), 500

@api.route('/auth/reset-password', methods=['POST'])
def reset_password():
    """Reset password with token"""
    data = request.get_json()
    
    if not all(k in data for k in ['token', 'new_password']):
        return jsonify({"error": "Missing required fields"}), 400
    
    user = User.query.filter_by(reset_token=data['token']).first()
    
    if not user:
        return jsonify({"error": "Invalid or expired reset token"}), 400
    
    # Check if token is expired
    if user.reset_token_expiry < datetime.utcnow():
        return jsonify({"error": "Reset token has expired"}), 400
    
    try:
        # Update password
        user.password = bcrypt.generate_password_hash(data['new_password']).decode('utf-8')
        user.reset_token = None
        user.reset_token_expiry = None
        db.session.commit()
        
        return jsonify({"message": "Password reset successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
