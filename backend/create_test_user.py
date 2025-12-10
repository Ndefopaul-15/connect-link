"""
Create a test user for testing login
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import User

app = create_app()

def create_test_user():
    with app.app_context():
        print("Creating test user...")
        print("=" * 50)
        
        # Check if user exists
        existing_user = User.query.filter_by(email='test@example.com').first()
        if existing_user:
            print("⚠ Test user already exists!")
            print(f"Email: test@example.com")
            print(f"Password: password123")
            return
        
        try:
            # Create test user
            user = User(
                email='test@example.com',
                password='password123'
            )
            
            db.session.add(user)
            db.session.commit()
            
            print("✅ Test user created successfully!")
            print()
            print("Login credentials:")
            print("  Email: test@example.com")
            print("  Password: password123")
            print()
            print("You can now login with these credentials!")
            
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error creating user: {e}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    create_test_user()
