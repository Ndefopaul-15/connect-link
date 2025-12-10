from datetime import date
from app import db
from sqlalchemy.orm import relationship

class LinkDailyStats(db.Model):
    __tablename__ = 'link_daily_stats'
    
    stat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link_id = db.Column(db.Integer, db.ForeignKey('link.link_id', ondelete='CASCADE'), nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today)
    total_clicks = db.Column(db.Integer, default=0)
    unique_clicks = db.Column(db.Integer, default=0)
    
    # Relationships
    link = relationship('Link', back_populates='daily_stats')
    
    # Indexes
    __table_args__ = (
        db.UniqueConstraint('link_id', 'date', name='_link_date_uc'),
    )
    
    def __init__(self, link_id, **kwargs):
        self.link_id = link_id
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def increment_clicks(self, is_unique=False):
        """Increment click counters"""
        self.total_clicks = (self.total_clicks or 0) + 1
        if is_unique:
            self.unique_clicks = (self.unique_clicks or 0) + 1
    
    def to_dict(self):
        return {
            'stat_id': self.stat_id,
            'link_id': self.link_id,
            'date': self.date.isoformat(),
            'total_clicks': self.total_clicks,
            'unique_clicks': self.unique_clicks
        }
