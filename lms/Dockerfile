# образ на основе которого создаём контейнер
FROM python:3.8.6-alpine

# рабочая директория внутри проекта
WORKDIR /home/project/lms

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для Postgre
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# устанавливаем зависимости
RUN pip install --upgrade pip
# копируем содержимое текущей папки в контейнер
COPY . .
RUN pip install -r req.txt

#RUN python manage.py migrate
#RUN python manage.py makemigrations bank
#RUN python manage.py migrate

RUN chmod +x ./entrypoint.sh
COPY ./entrypoint.sh ./usr/src/lms
ENTRYPOINT ["./entrypoint.sh"]