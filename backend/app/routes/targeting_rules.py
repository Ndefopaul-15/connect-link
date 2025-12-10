from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError

from .. import db
from ..models import Link, TargetingRule
from . import api


@api.route('/links/<string:slug>/targeting-rules', methods=['GET'])
@jwt_required()
def get_link_targeting_rules(slug):
    """List all targeting rules for a given link owned by the current user"""
    current_user_id = int(get_jwt_identity())

    link = Link.query.filter_by(short_url_slug=slug).first()
    if not link:
        return jsonify({"error": "Link not found"}), 404

    if link.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403

    rules = TargetingRule.query.filter_by(link_id=link.link_id).order_by(TargetingRule.priority.asc()).all()

    return jsonify({
        "rules": [rule.to_dict() for rule in rules]
    }), 200


@api.route('/links/<string:slug>/targeting-rules', methods=['POST'])
@jwt_required()
def create_targeting_rule(slug):
    """Create a new targeting rule for a link"""
    current_user_id = int(get_jwt_identity())
    data = request.get_json() or {}

    required_fields = ['targeting_type', 'criteria_value', 'redirect_url']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    link = Link.query.filter_by(short_url_slug=slug).first()
    if not link:
        return jsonify({"error": "Link not found"}), 404

    if link.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403

    try:
        rule = TargetingRule(
            link_id=link.link_id,
            targeting_type=data['targeting_type'],
            criteria_value=data['criteria_value'],
            redirect_url=data['redirect_url'],
            priority=data.get('priority', 1)
        )
        db.session.add(rule)
        db.session.commit()

        return jsonify({
            "message": "Targeting rule created successfully",
            "rule": rule.to_dict()
        }), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "A rule with this priority already exists for this link"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@api.route('/targeting-rules/<int:rule_id>', methods=['PUT'])
@jwt_required()
def update_targeting_rule(rule_id):
    """Update an existing targeting rule"""
    current_user_id = int(get_jwt_identity())
    data = request.get_json() or {}

    rule = TargetingRule.query.get(rule_id)
    if not rule:
        return jsonify({"error": "Rule not found"}), 404

    link = Link.query.get(rule.link_id)
    if not link or link.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403

    try:
        for field in ['targeting_type', 'criteria_value', 'redirect_url', 'priority']:
            if field in data:
                setattr(rule, field, data[field])

        db.session.commit()

        return jsonify({
            "message": "Targeting rule updated successfully",
            "rule": rule.to_dict()
        }), 200

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "A rule with this priority already exists for this link"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@api.route('/targeting-rules/<int:rule_id>', methods=['DELETE'])
@jwt_required()
def delete_targeting_rule(rule_id):
    """Delete a targeting rule"""
    current_user_id = int(get_jwt_identity())

    rule = TargetingRule.query.get(rule_id)
    if not rule:
        return jsonify({"error": "Rule not found"}), 404

    link = Link.query.get(rule.link_id)
    if not link or link.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403

    try:
        db.session.delete(rule)
        db.session.commit()
        return jsonify({"message": "Targeting rule deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
