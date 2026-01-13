#!/usr/bin/env bash
# Post-deploy script for Render

echo "🔍 Checking deployment status..."

echo "📊 Database status:"
python manage.py showmigrations

echo "👥 Checking users:"
python manage.py shell -c "
from django.contrib.auth.models import User
users = User.objects.all()
print(f'Total users: {users.count()}')
for user in users:
    print(f'- {user.username} (staff: {user.is_staff}, superuser: {user.is_superuser})')
"

echo "🏠 Checking lettings:"
python manage.py shell -c "
from lettings.models import Letting
print(f'Total lettings: {Letting.objects.count()}')
"

echo "👤 Checking profiles:"
python manage.py shell -c "
from profiles.models import Profile
print(f'Total profiles: {Profile.objects.count()}')
"

echo "✅ Post-deploy checks completed!"