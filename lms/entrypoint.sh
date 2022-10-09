#!/bin/sh
# Удаляем все старые данные
python manage.py flush --no-input
# Выполняем миграции
python manage.py migrate
python manage.py migrate sessions
python manage.py makemigrations
python manage.py makemigrations bank
python manage.py makemigrations polls
python manage.py migrate
python manage.py syncdb
python manage.py collectstatic

python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')"

exec "$@"