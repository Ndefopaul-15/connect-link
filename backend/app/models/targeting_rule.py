from .. import db
from sqlalchemy.orm import relationship, validates

class TargetingRule(db.Model):
    __tablename__ = 'targeting_rule'
    
    rule_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link_id = db.Column(db.Integer, db.ForeignKey('link.link_id', ondelete='CASCADE'), nullable=False)
    targeting_type = db.Column(db.String(50), nullable=False)  # 'country', 'device', 'language', etc.
    criteria_value = db.Column(db.String(255), nullable=False)  # The value to match against (e.g., 'US', 'mobile', 'es')
    redirect_url = db.Column(db.Text, nullable=False)
    priority = db.Column(db.Integer, default=1)
    
    # Relationships
    link = relationship('Link', back_populates='targeting_rules')
    
    # Indexes
    __table_args__ = (
        db.UniqueConstraint('link_id', 'priority', name='idx_unique_priority_per_link'),
    )
    
    def __repr__(self):
        return f'<TargetingRule {self.rule_id} for Link {self.link_id}'
    
    @validates('targeting_type')
    def validate_targeting_type(self, key, targeting_type):
        valid_types = ['country', 'device', 'language', 'os', 'browser', 'referrer']
        if targeting_type not in valid_types:
            raise ValueError(f"Invalid targeting type. Must be one of: {', '.join(valid_types)}")
        return targeting_type
    
    @validates('priority')
    def validate_priority(self, key, priority):
        if not isinstance(priority, int) or priority < 1:
            raise ValueError("Priority must be a positive integer")
        return priority
    
    def to_dict(self):
        return {
            'rule_id': self.rule_id,
            'link_id': self.link_id,
            'targeting_type': self.targeting_type,
            'criteria_value': self.criteria_value,
            'redirect_url': self.redirect_url,
            'priority': self.priority
        }
