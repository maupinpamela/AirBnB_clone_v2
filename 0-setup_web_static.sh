#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Holberton" | sudo tee /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
locations="\\\nlocation /hbnb_static/ {alias /data/web_static/current/;}"
sudo sed -i "37i $locations" /etc/nginx/sites-available/default
sudo service nginx restart
