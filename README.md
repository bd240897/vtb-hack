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

# Верстка проекта в figma
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


# Доска с идеями на миро
    https://miro.com/app/board/uXjVPP7sbA0=/?share_link_id=979095165470