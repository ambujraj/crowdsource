web: gunicorn crowdsource.wsgi
release: python manage.py makemigrations --merge
web: run-program waitress-serve --port=$PORT settings.wsgi:application
