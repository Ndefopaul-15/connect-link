from datetime import datetime
from app import db
from sqlalchemy.orm import relationship

class Click(db.Model):
    __tablename__ = 'click'
    __table_args__ = (
        db.Index('idx_click_link_id_time', 'link_id', 'click_date'),
    )
    
    click_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link_id = db.Column(db.Integer, db.ForeignKey('link.link_id', ondelete='CASCADE'), nullable=False)
    click_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    hashed_ip = db.Column(db.String(255))
    browser = db.Column(db.String(100))
    os = db.Column(db.String(100))
    country = db.Column(db.String(100))
    referrer = db.Column(db.Text)
    
    # Relationships
    link = relationship('Link', back_populates='clicks')
    
    def __init__(self, link_id, **kwargs):
        self.link_id = link_id
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dict(self):
        return {
            'click_id': self.click_id,
            'link_id': self.link_id,
            'click_date': self.click_date.isoformat(),
            'browser': self.browser,
            'os': self.os,
            'country': self.country,
            'referrer': self.referrer
        }
