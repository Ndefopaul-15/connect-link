from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from .. import db
from ..models import Link, QRCode
from . import api


@api.route('/links/<string:slug>/qr-code', methods=['GET'])
@jwt_required()
def get_qr_code(slug):
    """Get the QR code configuration for a link owned by the current user"""
    current_user_id = int(get_jwt_identity())

    link = Link.query.filter_by(short_url_slug=slug).first()
    if not link:
        return jsonify({"error": "Link not found"}), 404

    if link.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403

    qr_code = link.qr_code
    if not qr_code:
        return jsonify({"error": "QR code not found"}), 404

    return jsonify(qr_code.to_dict()), 200


@api.route('/links/<string:slug>/qr-code', methods=['POST', 'PUT'])
@jwt_required()
def upsert_qr_code(slug):
    """Create or update the QR code for a link owned by the current user"""
    current_user_id = int(get_jwt_identity())
    data = request.get_json() or {}

    if 'code_type' not in data:
        return jsonify({"error": "Missing required field: code_type"}), 400

    link = Link.query.filter_by(short_url_slug=slug).first()
    if not link:
        return jsonify({"error": "Link not found"}), 404

    if link.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403

    try:
        qr_code = link.qr_code
        if qr_code is None:
            qr_code = QRCode(
                link_id=link.link_id,
                code_type=data['code_type'],
                design_parameters=data.get('design_parameters')
            )
            db.session.add(qr_code)
        else:
            qr_code.code_type = data['code_type']
            if 'design_parameters' in data:
                qr_code.design_parameters = data['design_parameters']

        db.session.commit()

        return jsonify({
            "message": "QR code saved successfully",
            "qr_code": qr_code.to_dict()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
