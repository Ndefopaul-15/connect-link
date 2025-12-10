from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models import Link, Click
from . import api


@api.route('/links/<string:slug>/clicks', methods=['GET'])
@jwt_required()
def get_link_clicks(slug):
    """List click events for a link owned by the current user"""
    current_user_id = int(get_jwt_identity())

    link = Link.query.filter_by(short_url_slug=slug).first()
    if not link:
        return jsonify({"error": "Link not found"}), 404

    if link.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)

    query = Click.query.filter_by(link_id=link.link_id).order_by(Click.click_date.desc())
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    clicks = pagination.items

    return jsonify({
        "clicks": [click.to_dict() for click in clicks],
        "total": pagination.total,
        "pages": pagination.pages,
        "current_page": page
    }), 200
