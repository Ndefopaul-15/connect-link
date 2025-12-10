"""
Migration script to add password reset fields to User table
Run this script to update the database schema
"""
from app import app, db
from sqlalchemy import text

def migrate():
    with app.app_context():
        try:
            # Add reset_token column
            db.session.execute(text(
                "ALTER TABLE user ADD COLUMN reset_token VARCHAR(255)"
            ))
            print("✓ Added reset_token column")
        except Exception as e:
            print(f"reset_token column might already exist: {e}")
        
        try:
            # Add reset_token_expiry column
            db.session.execute(text(
                "ALTER TABLE user ADD COLUMN reset_token_expiry DATETIME"
            ))
            print("✓ Added reset_token_expiry column")
        except Exception as e:
            print(f"reset_token_expiry column might already exist: {e}")
        
        try:
            db.session.commit()
            print("\n✅ Migration completed successfully!")
            print("You can now use the forgot password feature.")
        except Exception as e:
            db.session.rollback()
            print(f"\n❌ Migration failed: {e}")

if __name__ == '__main__':
    print("Starting password reset migration...\n")
    migrate()
