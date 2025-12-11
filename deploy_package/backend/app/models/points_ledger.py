from datetime import datetime
from app import db

class PointsLedger(db.Model):
    __tablename__ = 'points_ledger'
    
    ledger_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)
    reward_id = db.Column(db.Integer, db.ForeignKey('reward.reward_id', ondelete='SET NULL'))
    points_amount = db.Column(db.Integer, nullable=False)  # Positive for earning, negative for spending
    transaction_type = db.Column(db.String(50), nullable=False)  # e.g., 'signup', 'referral', 'reward_redemption', etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', back_populates='point_transactions')
    reward = db.relationship('Reward', back_populates='point_transactions')
    
    def __init__(self, user_id, points_amount, transaction_type, **kwargs):
        self.user_id = user_id
        self.points_amount = points_amount
        self.transaction_type = transaction_type
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    @classmethod
    def create_transaction(cls, user, points_amount, transaction_type, **kwargs):
        """Create a new transaction and update user's point balance"""
        transaction = cls(
            user_id=user.user_id,
            points_amount=points_amount,
            transaction_type=transaction_type,
            **kwargs
        )
        
        db.session.add(transaction)
        user.update_points(points_amount)
        return transaction
    
    def to_dict(self):
        return {
            'ledger_id': self.ledger_id,
            'user_id': self.user_id,
            'reward_id': self.reward_id,
            'points_amount': self.points_amount,
            'transaction_type': self.transaction_type,
            'created_at': self.created_at.isoformat()
        }
