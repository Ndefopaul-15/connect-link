from app import db
from sqlalchemy.orm import relationship

class Domain(db.Model):
    __tablename__ = 'domain'
    
    domain_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    domain_name = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)
    status = db.Column(db.String(50), default='Pending')
    
    # Relationships
    user = relationship('User', back_populates='domains')
    links = relationship('Link', back_populates='domain', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'domain_id': self.domain_id,
            'domain_name': self.domain_name,
            'user_id': self.user_id,
            'status': self.status
        }
