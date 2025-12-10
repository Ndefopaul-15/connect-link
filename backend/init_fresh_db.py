"""
Initialize a fresh database with all tables
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import User

app = create_app()

def init_db():
    with app.app_context():
        print("Initializing fresh database...")
        print("=" * 50)
        
        # Drop all tables
        print("Dropping all existing tables...")
        db.drop_all()
        
        # Create all tables with new schema
        print("Creating all tables with updated schema...")
        db.create_all()
        
        print("✅ Database initialized successfully!")
        print()
        print("All tables created with:")
        print("  - user (with reset_token and reset_token_expiry)")
        print("  - link")
        print("  - domain")
        print("  - click")
        print("  - qr_code")
        print("  - targeting_rule")
        print("  - link_daily_stats")
        print("  - reward")
        print("  - points_ledger")
        print()
        print("✅ You can now register and login!")

if __name__ == '__main__':
    init_db()
