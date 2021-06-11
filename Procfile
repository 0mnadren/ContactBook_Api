release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn simple_address_management.wsgi
