#!/usr/bin/env bash
# Debug script to check user status

# Get Python executable
PYTHON_CMD="/Users/steveraffner/Desktop/oc-lettings/venv/bin/python"

echo "🔍 Environment variables:"
echo "DJANGO_SUPERUSER_USERNAME: ${DJANGO_SUPERUSER_USERNAME:-admin}"
echo "DJANGO_SUPERUSER_EMAIL: ${DJANGO_SUPERUSER_EMAIL:-admin@example.com}"
echo "DJANGO_SUPERUSER_PASSWORD: ${DJANGO_SUPERUSER_PASSWORD:+***SET***}"

echo ""
echo "👥 All users in database:"
$PYTHON_CMD manage.py shell -c "
from django.contrib.auth.models import User
for user in User.objects.all():
    print(f'- Username: {user.username}, Email: {user.email}')
    print(f'  Staff: {user.is_staff}, Superuser: {user.is_superuser}')
    print(f'  Active: {user.is_active}, Last login: {user.last_login}')
    print('---')
if not User.objects.exists():
    print('No users found in database!')
"

echo ""
echo "🔐 Test admin login:"
$PYTHON_CMD manage.py shell -c "
from django.contrib.auth import authenticate
username = 'admin'
password = 'Abc1234!'
user = authenticate(username=username, password=password)
if user:
    print(f'✅ Authentication successful for {username}')
    print(f'User active: {user.is_active}, staff: {user.is_staff}, superuser: {user.is_superuser}')
else:
    print(f'❌ Authentication failed for {username}')
    from django.contrib.auth.models import User
    try:
        user = User.objects.get(username=username)
        print(f'User exists but password incorrect. Active: {user.is_active}')
    except User.DoesNotExist:
        print(f'User {username} does not exist in database')
"