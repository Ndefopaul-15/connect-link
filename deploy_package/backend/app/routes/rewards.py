from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from .. import db
from ..models import Reward, User, PointsLedger
from . import api


@api.route('/rewards', methods=['GET'])
@jwt_required()
def list_rewards():
    """List all available rewards"""
    rewards = Reward.query.order_by(Reward.points_cost.asc()).all()
    return jsonify({
        "rewards": [reward.to_dict() for reward in rewards]
    }), 200


@api.route('/rewards/redeem', methods=['POST'])
@jwt_required()
def redeem_reward():
    """Redeem a reward using the current user's points balance"""
    current_user_id = int(get_jwt_identity())
    data = request.get_json() or {}

    reward_id = data.get('reward_id')
    if not reward_id:
        return jsonify({"error": "Missing required field: reward_id"}), 400

    user = User.query.get(current_user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    reward = Reward.query.get(reward_id)
    if not reward:
        return jsonify({"error": "Reward not found"}), 404

    if user.point_balance < reward.points_cost:
        return jsonify({"error": "Insufficient points"}), 400

    try:
        transaction = PointsLedger.create_transaction(
            user=user,
            points_amount=-reward.points_cost,
            transaction_type='reward_redemption',
            reward_id=reward.reward_id
        )
        db.session.commit()

        return jsonify({
            "message": "Reward redeemed successfully",
            "transaction": transaction.to_dict(),
            "user": user.to_dict()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
