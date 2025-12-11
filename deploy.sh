#!/bin/bash

echo "🚀 Deploying Connect Link to conlk.zen-apps.com..."
echo ""

SERVER="conlkaccountftp@conlk.zen-apps.com"
REMOTE_PATH="/conlk.zen-apps.com"

# Upload backend files
echo "📤 Uploading backend files..."
scp -r backend/app "$SERVER:$REMOTE_PATH/"
scp backend/wsgi.py "$SERVER:$REMOTE_PATH/"
scp backend/.htaccess "$SERVER:$REMOTE_PATH/"
scp backend/.env.production "$SERVER:$REMOTE_PATH/.env"
scp backend/requirements.production.txt "$SERVER:$REMOTE_PATH/requirements.txt"
scp backend/init_database.py "$SERVER:$REMOTE_PATH/"

echo ""
echo "📤 Uploading frontend files..."
scp -r frontend/dist/* "$SERVER:$REMOTE_PATH/"

echo ""
echo "⚙️  Configuring server..."
ssh "$SERVER" << 'EOF'
cd /conlk.zen-apps.com
echo "Installing Python dependencies..."
python3 -m pip install -r requirements.txt --user
echo "Initializing database..."
python3 init_database.py
echo "Setting permissions..."
chmod 755 wsgi.py
chmod 644 .htaccess
chmod 600 .env
echo "Server configuration complete!"
EOF

echo ""
echo "✅ Deployment complete!"
echo "🌐 Visit: https://conlk.zen-apps.com"
echo ""
