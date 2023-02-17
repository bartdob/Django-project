release: python manage.py migrate --run-syncdb
web: gunicorn PROJECT.wsgi
worker: celery -A PROJECT worker -B -l info
