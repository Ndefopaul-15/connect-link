"""
Fix Invalid Slugs in Database
This script finds and fixes links with invalid slugs (containing spaces or special characters)
"""

from app import create_app, db
from app.models import Link
import re

def fix_slugs():
    app = create_app()
    
    with app.app_context():
        # Find all links
        links = Link.query.all()
        
        print(f"Found {len(links)} links in database\n")
        
        fixed_count = 0
        for link in links:
            # Check if slug has spaces or invalid characters
            if ' ' in link.short_url_slug or not re.match(r'^[a-zA-Z0-9_-]+$', link.short_url_slug):
                old_slug = link.short_url_slug
                
                # Fix the slug: replace spaces with hyphens, remove invalid chars
                new_slug = re.sub(r'[^a-zA-Z0-9_-]', '-', link.short_url_slug)
                new_slug = re.sub(r'-+', '-', new_slug)  # Remove multiple hyphens
                new_slug = new_slug.strip('-')  # Remove leading/trailing hyphens
                
                # Make sure it's unique
                counter = 1
                base_slug = new_slug
                while Link.query.filter_by(short_url_slug=new_slug).first():
                    new_slug = f"{base_slug}-{counter}"
                    counter += 1
                
                print(f"Fixing slug: '{old_slug}' → '{new_slug}'")
                
                # Update the link
                link.short_url_slug = new_slug
                link.short_url = f"http://127.0.0.1:5000/api/{new_slug}"
                
                fixed_count += 1
        
        if fixed_count > 0:
            db.session.commit()
            print(f"\n✅ Fixed {fixed_count} invalid slugs!")
        else:
            print("✅ No invalid slugs found!")
        
        # Show all links
        print("\n📋 Current links in database:")
        links = Link.query.all()
        for link in links:
            print(f"  - Slug: '{link.short_url_slug}' → {link.long_url}")

if __name__ == '__main__':
    fix_slugs()
