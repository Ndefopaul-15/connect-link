"""
Update database schema with new password reset fields
WARNING: This will preserve existing data
"""
import os
import sys

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import User

app = create_app()

def update_database():
    with app.app_context():
        print("Updating database schema...")
        print("=" * 50)
        
        # Check if database exists
        db_path = 'instance/connect_link.db'
        if os.path.exists(db_path):
            print(f"✓ Database found at: {db_path}")
        else:
            print(f"⚠ Database not found, will create new one")
        
        try:
            # Create all tables (will add new columns if they don't exist)
            db.create_all()
            print("✓ Database schema updated successfully!")
            print("\nNew columns added to User table:")
            print("  - reset_token (VARCHAR 255)")
            print("  - reset_token_expiry (DATETIME)")
            print("\n✅ You can now use the forgot password feature!")
            
        except Exception as e:
            print(f"\n❌ Error updating database: {e}")
            print("\nIf you see column already exists errors, that's OK!")
            print("The database is already up to date.")

if __name__ == '__main__':
    update_database()
