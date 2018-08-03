#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

sudo apt-get update -y
sudo apt-get install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
locations="\\\nlocation /hbnb_static/ {alias /data/web_static/current/;}"
sed -i "37i $locations" /etc/nginx/sites-available/default
sudo service nginx restart
