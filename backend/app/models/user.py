from datetime import datetime
from app import db, bcrypt
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'user'
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    subscription_plan = db.Column(db.String(50), nullable=False, default='Free')
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    point_balance = db.Column(db.Integer, default=0)
    reset_token = db.Column(db.String(255), nullable=True)
    reset_token_expiry = db.Column(db.DateTime, nullable=True)
    
    # Relationships
    domains = relationship('Domain', back_populates='user', cascade='all, delete-orphan')
    links = relationship('Link', back_populates='user', cascade='all, delete-orphan')
    point_transactions = relationship('PointsLedger', back_populates='user')
    
    def __init__(self, email, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    def update_points(self, amount):
        """Update user's point balance"""
        self.point_balance += amount
        return self.point_balance
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'subscription_plan': self.subscription_plan,
            'creation_date': self.creation_date.isoformat(),
            'is_active': self.is_active,
            'point_balance': self.point_balance
        }
