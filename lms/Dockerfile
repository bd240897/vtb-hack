# образ на основе которого создаём контейнер
FROM python:3.8.6-alpine

# рабочая директория внутри проекта
# ВНИМЕНИЕ - МЫ копирвем ТУТ только ТЕ файлы рядом с которыми тусит DockerFile!!!!!!!!!!!!!!!
# т.е. в папке будет (пример) /usr/src/mysite/manage.py
WORKDIR /usr/src/lms

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для Postgre
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r req.txt

# копируем содержимое текущей папки в контейнер
COPY . .

RUN python manage.py migrate
RUN python makemigrations bank
RUN python manage.py migrate