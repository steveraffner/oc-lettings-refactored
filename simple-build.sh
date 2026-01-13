#!/usr/bin/env bash
# Simple build script for Render free plan

set -o errexit

echo "🔧 Installing dependencies..."
pip install -r requirements.txt

echo "🗃️ Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "🔄 Running migrations..."
python manage.py migrate --noinput

echo "✅ Build completed!"

# Les commandes de création d'utilisateur se feront via la migration et le wsgi.py