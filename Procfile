web: gunicorn crowdsource.wsgi
release: python manage.py migrate
web: run-program waitress-serve --port=$PORT settings.wsgi:application
