worker: celery -A PROJECT worker -B --loglevel=info
release: python manage.py migrate
web: gunicorn PROJECT.wsgi