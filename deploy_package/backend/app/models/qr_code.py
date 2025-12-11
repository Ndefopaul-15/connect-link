from app import db
from sqlalchemy.orm import relationship

class QRCode(db.Model):
    __tablename__ = 'qr_code'
    
    link_id = db.Column(db.Integer, db.ForeignKey('link.link_id', ondelete='CASCADE'), primary_key=True)
    code_type = db.Column(db.String(50), nullable=False)
    design_parameters = db.Column(db.Text)  # JSON string of design parameters
    
    # Relationships
    link = relationship('Link', back_populates='qr_code')
    
    def to_dict(self):
        return {
            'link_id': self.link_id,
            'code_type': self.code_type,
            'design_parameters': self.design_parameters
        }
