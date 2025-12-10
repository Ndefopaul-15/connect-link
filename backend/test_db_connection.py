#!/usr/bin/env python3
"""
Script pour tester la connexion à la base de données MariaDB de production
"""
import sys

try:
    import pymysql
except ImportError:
    print("❌ PyMySQL n'est pas installé!")
    print("Installez-le avec: pip install pymysql")
    sys.exit(1)

# Informations de connexion
DB_CONFIG = {
    'host': 'localhost',
    'user': 'conlkdbuser',
    'password': 'l0X&Vo$6pok0Wqii',
    'database': 'conlkdb',
    'port': 3306
}

print("=" * 60)
print("TEST DE CONNEXION À LA BASE DE DONNÉES MARIADB")
print("=" * 60)
print(f"\nHôte: {DB_CONFIG['host']}")
print(f"Base de données: {DB_CONFIG['database']}")
print(f"Utilisateur: {DB_CONFIG['user']}")
print(f"Port: {DB_CONFIG['port']}")
print("\nConnexion en cours...\n")

try:
    # Tentative de connexion
    connection = pymysql.connect(**DB_CONFIG)
    
    print("✅ CONNEXION RÉUSSIE!")
    
    # Test d'une requête simple
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"✅ Version MariaDB: {version[0]}")
        
        # Lister les tables existantes
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        if tables:
            print(f"\n📋 Tables existantes ({len(tables)}):")
            for table in tables:
                print(f"   - {table[0]}")
        else:
            print("\n⚠️  Aucune table trouvée (normal pour une nouvelle base)")
    
    connection.close()
    print("\n" + "=" * 60)
    print("✓ Test terminé avec succès!")
    print("=" * 60)
    
except pymysql.err.OperationalError as e:
    print(f"❌ ERREUR DE CONNEXION: {e}")
    print("\nVérifiez:")
    print("  1. Que le serveur MariaDB est accessible")
    print("  2. Que les identifiants sont corrects")
    print("  3. Que la base de données existe")
    sys.exit(1)
    
except Exception as e:
    print(f"❌ ERREUR INATTENDUE: {e}")
    sys.exit(1)
