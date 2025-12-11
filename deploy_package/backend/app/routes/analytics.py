from datetime import datetime

from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models import Link, LinkDailyStats
from . import api


@api.route('/links/<string:slug>/stats/daily', methods=['GET'])
@jwt_required()
def get_link_daily_stats(slug):
    """Return daily aggregated stats for a link"""
    current_user_id = int(get_jwt_identity())

    link = Link.query.filter_by(short_url_slug=slug).first()
    if not link:
        return jsonify({"error": "Link not found"}), 404

    if link.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403

    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')

    query = LinkDailyStats.query.filter_by(link_id=link.link_id)

    def parse_date(value: str):
        return datetime.strptime(value, "%Y-%m-%d").date()

    try:
        if start_date_str:
            start_date = parse_date(start_date_str)
            query = query.filter(LinkDailyStats.date >= start_date)
        if end_date_str:
            end_date = parse_date(end_date_str)
            query = query.filter(LinkDailyStats.date <= end_date)
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    stats = query.order_by(LinkDailyStats.date.asc()).all()

    return jsonify({
        "stats": [stat.to_dict() for stat in stats]
    }), 200


@api.route('/links/<string:slug>/stats/summary', methods=['GET'])
@jwt_required()
def get_link_stats_summary(slug):
    """Return a summary of total and unique clicks for a link"""
    current_user_id = int(get_jwt_identity())

    link = Link.query.filter_by(short_url_slug=slug).first()
    if not link:
        return jsonify({"error": "Link not found"}), 404

    if link.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403

    total_clicks = sum(stat.total_clicks or 0 for stat in link.daily_stats)
    unique_clicks = sum(stat.unique_clicks or 0 for stat in link.daily_stats)

    return jsonify({
        "link_id": link.link_id,
        "short_url_slug": link.short_url_slug,
        "total_clicks": total_clicks,
        "unique_clicks": unique_clicks
    }), 200
