#!/usr/bin/env python3
"""
Initialize Production Database on conlk.zen-apps.com
This script creates all necessary tables in the MariaDB database
"""
import sys
import os

# Add backend to path
backend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend')
sys.path.insert(0, backend_dir)

# Set environment variables for production database
os.environ['FLASK_ENV'] = 'production'
os.environ['DATABASE_URL'] = 'mysql+pymysql://conlkdbuser:l0X&Vo$6pok0Wqii@conlk.zen-apps.com:3306/conlkdb'
os.environ['SECRET_KEY'] = '0cc77ae1bbdda1c1a89d087550cd5bedc6abe27bf022051ae2d9095a17c8b3ee'
os.environ['JWT_SECRET_KEY'] = '3e37307a56af10b69cd3a26a396b1bae4e62151a94480002c1aea3e82b21bbfb'

from app import create_app, db

def init_database():
    """Initialize the production database"""
    print("🔧 Initializing production database...")
    print(f"📍 Database: conlk.zen-apps.com:3306/conlkdb")
    
    # Create Flask app
    app = create_app('production')
    
    with app.app_context():
        try:
            # Create all tables
            print("📊 Creating database tables...")
            db.create_all()
            print("✅ Database tables created successfully!")
            
            # Verify tables were created
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            
            print(f"\n✅ Created {len(tables)} tables:")
            for table in tables:
                print(f"   - {table}")
            
            print("\n🎉 Database initialization complete!")
            return True
            
        except Exception as e:
            print(f"\n❌ Error initializing database: {str(e)}")
            return False

if __name__ == "__main__":
    success = init_database()
    sys.exit(0 if success else 1)
