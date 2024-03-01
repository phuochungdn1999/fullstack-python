#!/bin/sh

sleep 20

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell 
python3 manage.py runserver 0.0.0.0:8080