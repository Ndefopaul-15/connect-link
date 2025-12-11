from app import db

class Reward(db.Model):
    __tablename__ = 'reward'
    
    reward_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    points_cost = db.Column(db.Integer, nullable=False)
    
    # Relationships
    point_transactions = db.relationship('PointsLedger', back_populates='reward')
    
    def to_dict(self):
        return {
            'reward_id': self.reward_id,
            'name': self.name,
            'description': self.description,
            'points_cost': self.points_cost
        }
