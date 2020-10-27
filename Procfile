release: python manage.py migrate
web: gunicorn PROJECT.wsgi
worker: celery -A PROJECT worker -B -l info -b --loglevel=info