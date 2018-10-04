ENV_MODE="dev"
SERVICE="django"
CONTAINER_NAME=${ENV_MODE}-${SERVICE}
IMG_NAME="local"

DJANGO_CONTAINER_NAME=`docker ps | grep nomadgram_web | awk '{print $$1}'`
DB_CONTAINER_NAME=`docker ps | grep postgres | awk '{print $$1}'`
SOURCE_DIR=`pwd`


exec-django-root:
	docker exec  -it $(DJANGO_CONTAINER_NAME)  /bin/bash
	
exec-django:
	docker exec -u $(USER) -it $(DJANGO_CONTAINER_NAME)  /bin/bash
	
#exec-db:
#	docker exec -u negabaro -it $(DB_CONTAINER_NAME) /bin/bash

build-run:
	if [ `docker ps -q -f name=${CONTAINER_NAME}` ]; then docker rm -f ${CONTAINER_NAME}; fi
	docker build -t ${IMG_NAME}/${CONTAINER_NAME} --file Dockerfile .
	docker run  --rm  --name ${CONTAINER_NAME} -v `pwd`:/code:cached  -p 8000:8000    ${IMG_NAME}/${CONTAINER_NAME}


run-compose:
	docker-compose up --build
	
run-test:
	if [ `docker ps -q -f name=${CONTAINER_NAME}` ]; then docker rm -f ${CONTAINER_NAME}; fi
	#docker build -t ${IMG_NAME}/${CONTAINER_NAME} --file Dockerfile .
	docker run  -it  --name ${CONTAINER_NAME} -v `pwd`:/code:cached  -p 8000:8000  ${IMG_NAME}/${CONTAINER_NAME} sh