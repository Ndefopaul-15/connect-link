#!/usr/bin/env python3
"""
Script pour générer des clés secrètes sécurisées pour la production
"""
import secrets

print("=" * 60)
print("CLÉS SECRÈTES POUR LA PRODUCTION")
print("=" * 60)
print("\n⚠️  IMPORTANT: Copiez ces clés dans votre fichier .env sur le serveur")
print("⚠️  Ne partagez JAMAIS ces clés publiquement!\n")

secret_key = secrets.token_hex(32)
jwt_secret_key = secrets.token_hex(32)

print(f"SECRET_KEY={secret_key}")
print(f"JWT_SECRET_KEY={jwt_secret_key}")

print("\n" + "=" * 60)
print("✓ Clés générées avec succès!")
print("=" * 60)
