# О проекте vtv-hack

Трек - Web

Задача - Разработать веб-сервис с элементами геймификации для вовлечения сотрудников Банка ВТБ во внутрикорпоративные активности

## Инструменты
- python 3.8
- django 4
- PostgreSQL
- Docker
- Bootstrap 5

# Запуск через Docker (VPS in https://cloud.yandex.ru/)

## 1. Установка Docker (Ubuntu 20.04) 
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru

    sudo apt update
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
    sudo apt update
    apt-cache policy docker-ce
    sudo apt install docker-ce
    sudo systemctl status docker // status

## 2. Установка Docker-compose (Ubuntu 20.04)
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-ru

sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version // status


## 3. Запуск проекта 

    git clone https://github.com/bd240897/vtb-hack.git
    cd ./vtb-hack/
    docker-compose -f docker-compose.yml up --build -d

# 4. another 

    sudo -i // войти под админа
    password // сменить пароль админу

# Запуск на Windows
    git clone https://github.com/bd240897/vtb-hack.git
    python -m venv venv
    venv\Scripts\activate.bat
    cd vtb-hack\lms
    pip install -r req.txt
    python manage.py migrate
    python manage.py makemigrations bank
    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser
    python manage.py runserver

# Материалы проекта 

## Верстка проекта в figma
    https://www.figma.com/file/TgSW8pv0zzggm4yk43SHhd/ВТБ?node-id=0%3A1
# Запуск через Docker
    sudo apt update
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
    apt-cache policy docker-ce
    sudo apt install docker-ce
    git clone https://github.com/bd240897/vtb-hack.git
    cd ./vtb-hack/
    docker-compose up


## Доска с идеями на миро
    https://miro.com/app/board/uXjVPP7sbA0=/?share_link_id=9790951654700