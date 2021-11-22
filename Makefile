SHELL := /bin/bash
.PHONY: all, deploy, modules

all: deploy

deploy:
	python3 install_api.py
	# Create SAM-API Docker Image
	sudo docker build -t sam-api .
	# Deploy container with image
	sudo docker run --name sam-api -p 8080:8080 -v "$(shell pwd)/":/api/ -d sam-api 
	# Create SAM-DB Docker Image Running MariaDB
	sudo docker build -t sam-db database/
	# Deploy container with image using the default password 'secure' for user root
	sudo docker run --name sam-db -e MYSQL_ROOT_PASSWORD=secure -p 3306:3306 -d sam-db
	# Create network between containers, the sam-api container needs to access the Maria database that is available on the sam-db container 
	sudo docker network create sam-network
	sudo docker network connect sam-network sam-db
	sudo docker network connect sam-network sam-api
	@echo "[SAM] Backend deployed for development (http://localhost:8080/)! Have a nice day!"

modules:
	# Run a sql script against the sam-db container. See docs for this.
	sudo docker exec -it sam-db python3 install_db.py && docker exec -i sam-db sh -c 'exec mysql -uroot -psecure' < database/database-core-modules.sql
	# Unzip .core-modules.zip in the external folder
	unzip external/.core-modules.zip -d external/ 
	@echo "[SAM] Core modules deployed for development (http://localhost:8080/)! Have a nice day!"

# TODO: clean