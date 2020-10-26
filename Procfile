celeryd: celery -A PROJECT worker -B -l info
release: python manage.py migrate
web: gunicorn PROJECT.wsgi