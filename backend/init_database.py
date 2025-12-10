#!/usr/bin/env python3
"""
Database Initialization Script for Production
Creates all tables in the MariaDB database
"""
import os
import sys

# Set production environment
os.environ['FLASK_ENV'] = 'production'

try:
    from app import create_app, db
    from app.models import User, Link, Domain, QRCode, TargetingRule, Click, LinkDailyStats, Reward
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    print("Assurez-vous d'être dans le bon répertoire et que toutes les dépendances sont installées.")
    sys.exit(1)

def init_database():
    """Initialize the database with all tables"""
    print("=" * 70)
    print("INITIALISATION DE LA BASE DE DONNÉES - PRODUCTION")
    print("=" * 70)
    
    # Create Flask app
    app = create_app('production')
    
    with app.app_context():
        try:
            # Get database URI
            db_uri = app.config.get('SQLALCHEMY_DATABASE_URI', 'Not configured')
            print(f"\n📊 Base de données: {db_uri.split('@')[1] if '@' in db_uri else db_uri}")
            
            print("\n🔧 Création des tables...")
            
            # Create all tables
            db.create_all()
            
            print("✅ Tables créées avec succès!")
            
            # List all tables
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            
            print(f"\n📋 Tables créées ({len(tables)}):")
            for table in tables:
                print(f"   ✓ {table}")
            
            # Create a test admin user (optional)
            create_test_user = input("\n❓ Créer un utilisateur admin de test? (y/n): ").lower()
            
            if create_test_user == 'y':
                from werkzeug.security import generate_password_hash
                
                email = input("Email: ")
                password = input("Mot de passe: ")
                
                # Check if user exists
                existing_user = User.query.filter_by(email=email).first()
                if existing_user:
                    print("⚠️  Cet utilisateur existe déjà!")
                else:
                    user = User(
                        email=email,
                        password_hash=generate_password_hash(password)
                    )
                    db.session.add(user)
                    db.session.commit()
                    print(f"✅ Utilisateur créé: {email}")
            
            print("\n" + "=" * 70)
            print("✓ Initialisation terminée avec succès!")
            print("=" * 70)
            
        except Exception as e:
            print(f"\n❌ ERREUR: {e}")
            print("\nVérifiez:")
            print("  1. Que la base de données existe")
            print("  2. Que les credentials sont corrects dans .env")
            print("  3. Que MariaDB est accessible")
            sys.exit(1)

if __name__ == "__main__":
    init_database()
