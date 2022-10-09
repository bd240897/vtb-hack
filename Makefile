up:
	docker-compose -f docker-compose.test.yml up -d --build

down:
	sudo docker stop $$(docker ps -a -q)

cl:
	sudo docker system prune && sudo docker volume prune
