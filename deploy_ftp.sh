#!/bin/bash

echo "🚀 Deploying Connect Link via FTP..."
echo ""

FTP_HOST="conlk.zen-apps.com"
FTP_USER="conlkaccountftp"
FTP_PASS="1xbz22B0?"
REMOTE_DIR="/conlk.zen-apps.com"

# Create FTP command file
cat > ftp_commands.txt << EOF
open $FTP_HOST
user $FTP_USER $FTP_PASS
binary
cd $REMOTE_DIR

# Create directories if needed
mkdir app
mkdir app/models
mkdir app/routes
mkdir assets

# Upload backend files
lcd backend
put wsgi.py
put .htaccess
put init_database.py

# Rename and upload env
put .env.production .env
put requirements.production.txt requirements.txt

# Upload app folder files
cd app
lcd app
put __init__.py
put config.py

# Upload models
cd models
lcd models
mput *.py

# Go back and upload routes
cd ..
cd ..
cd routes
lcd ../routes
mput *.py

# Upload frontend
cd $REMOTE_DIR
lcd ../../frontend/dist
put index.html
cd assets
lcd assets
mput *

bye
EOF

# Execute FTP commands
ftp -inv < ftp_commands.txt

# Clean up
rm ftp_commands.txt

echo ""
echo "✅ Upload complete!"
echo "🌐 Visit: https://conlk.zen-apps.com"
