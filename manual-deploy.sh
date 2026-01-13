#!/usr/bin/env bash
# Manual deployment script for Render

echo "🔧 Manual Django Setup on Render"

echo "🗃️ Running migrations..."
python manage.py migrate --noinput

echo "👤 Resetting superuser..."
python manage.py reset_superuser

echo "📊 Creating sample data..."
python manage.py create_sample_data

echo "✅ Manual setup completed!"
echo ""
echo "🔐 Login credentials:"
echo "- Username: admin"
echo "- Password: Abc1234!"
echo "- URL: https://oc-lettings-av9a.onrender.com/admin/"