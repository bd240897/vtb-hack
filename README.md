# vtv-hack

Трек - Web

Задача - Разработать веб-сервис с элементами геймификации для вовлечения сотрудников Банка ВТБ во внутрикорпоративные активности

# Инструменты

python 3.8, django 4

# Запуск на Windows
    git clone https://github.com/bd240897/vtb-hack.git
    python -m venv venv
    venv\Scripts\activate.bat
    pip install -r req.txt
    python manage.py migrate
    python manage.py makemigrations bank
    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser
    python manage.py runserver

# Точка входа
    http://127.0.0.1:8000/bank/main


