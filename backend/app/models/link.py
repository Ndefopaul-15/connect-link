from datetime import datetime
from app import db
from sqlalchemy.orm import relationship
import shortuuid

class Link(db.Model):
    __tablename__ = 'link'
    __table_args__ = (
        db.Index('idx_link_slug', 'short_url_slug'),
    )
    
    link_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    long_url = db.Column(db.Text, nullable=False)
    short_url_slug = db.Column(db.String(20), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)
    domain_id = db.Column(db.Integer, db.ForeignKey('domain.domain_id', ondelete='SET NULL'))
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    expiration_date = db.Column(db.DateTime)
    is_dynamic = db.Column(db.Boolean, default=False)
    
    # Relationships
    user = relationship('User', back_populates='links')
    domain = relationship('Domain', back_populates='links')
    qr_code = relationship('QRCode', back_populates='link', uselist=False, cascade='all, delete-orphan')
    targeting_rules = relationship('TargetingRule', back_populates='link', cascade='all, delete-orphan')
    clicks = relationship('Click', back_populates='link', cascade='all, delete-orphan')
    daily_stats = relationship('LinkDailyStats', back_populates='link', cascade='all, delete-orphan')
    
    def __init__(self, **kwargs):
        super(Link, self).__init__(**kwargs)
        if not self.short_url_slug:
            self.short_url_slug = self._generate_short_slug()
    
    def _generate_short_slug(self, length=8):
        """Generate a short, unique slug for the short URL"""
        while True:
            slug = shortuuid.ShortUUID().random(length=length)
            if not Link.query.filter_by(short_url_slug=slug).first():
                return slug
    
    def get_short_url(self):
        """Return the full short URL with domain if available"""
        if self.domain:
            return f"https://{self.domain.domain_name}/{self.short_url_slug}"
        # Default domain - ALWAYS use Render URL
        # This ensures we never use localhost in production
        default_domain = 'https://connect-link.onrender.com'
        return f"{default_domain}/{self.short_url_slug}"
    
    def is_expired(self):
        """Check if the link has expired"""
        if self.expiration_date:
            return datetime.utcnow() > self.expiration_date
        return False
    
    def to_dict(self):
        return {
            'link_id': self.link_id,
            'long_url': self.long_url,
            'short_url': self.get_short_url(),
            'short_url_slug': self.short_url_slug,
            'user_id': self.user_id,
            'domain_id': self.domain_id,
            'creation_date': self.creation_date.isoformat(),
            'expiration_date': self.expiration_date.isoformat() if self.expiration_date else None,
            'is_dynamic': self.is_dynamic,
            'click_count': len(self.clicks),
            'is_active': not self.is_expired()
        }
