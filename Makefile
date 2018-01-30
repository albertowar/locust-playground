build:
	docker build -f Dockerfile.slave -t locust-slave .
	docker build -f Dockerfile.master -t locust-master .
	docker build -f Dockerfile.standalone -t locust-standalone .
	docker build -f Dockerfile.server -t server .

run:
	docker run -p 3000:3000 server --name server
	docker run -p 8089:8089 locust-master --name locust-master
	docker run locust-slave --name locust-slave0
	docker run locust-slave --name locust-slave1