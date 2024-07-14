#!/usr/bin/env bash
#Settng up new server

# shellcheck disable=SC2154
# shellcheck disable=SC1004

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file
sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Create symbolic link (delete and recreate if already exists)
if [ -L "/data/web_static/current" ]; then
    sudo rm "/data/web_static/current"
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content to hbnb_static
sudo tee /etc/nginx/sites-available/hbnb_static > /dev/null <<EOF
server {
    listen 80;
    listen [::]:80;

    server_name cityspaces.tech www.cityspaces.tech 100.26.247.135 18.235.248.212;

    location /hbnb_static {
        alias /data/web_static/current;
    }

    location / {
        return 404;
    }
}

server {
    listen 80;
    listen [::]:80;

    server_name localhost;

    location /hbnb_static {
        alias /data/web_static/current;
    }

    location / {
        return 404;
    }
}
EOF

sed -i '/http {/ {
    a\
        include /etc/nginx/sites-available/hbnb_static;
}' /etc/nginx/nginx.conf

# Create symbolic link to enable the new configuration
sudo ln -sf /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/

# Restart Nginx
sudo service nginx restart
