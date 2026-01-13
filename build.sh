#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit  # Exit on any error

echo "🔧 Installing dependencies..."
pip install -r requirements.txt

echo "🗃️ Collecting static files..."
python manage.py collectstatic --noinput

echo "🔄 Running migrations..."
python manage.py migrate

echo "👤 Resetting and creating superuser..."
python manage.py reset_superuser

echo "📊 Creating sample data..."
python manage.py create_sample_data

echo "✅ Build completed successfully!"