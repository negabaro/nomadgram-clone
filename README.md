ENV_MODE="dev"
SERVICE="django"
CONTAINER_NAME=${ENV_MODE}-${SERVICE}

run-test:
	if [ `docker ps -q -f name=${CONTAINER_NAME}` ]; then docker rm -f ${CONTAINER_NAME}; fi
	#docker build -t ${IMG_NAME}/${CONTAINER_NAME} --file Dockerfile .
	docker run  -it  --name ${CONTAINER_NAME} -v `pwd`:/pets-server:cached  -p 8000:8000  python:3.5.6-alpine3.7 sh
     docker run  -it  --name dev-django -v `pwd`:/pets-server:cached  -p 8000:8000  python:3.5.6-alpine3.7 sh


pip-install:
    apk add postgresql-dev libffi build-base libffi-dev python-dev py-pip jpeg-dev zlib-dev 
    apk add git <<필수는아님 
    pip install -r requirements.txt
    pip install pipenv django==1.10.8
    pipenv install
    
    python manage.py runserver 0.0.0.0:8000
    
Failed building wheel for Pillow
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

ImportError: No module named 'debug_toolbar'
pip install django-debug-toolbar

ImportError: No module named 'django_extensions'
^C/pets-server # pip install django_extensions


ImportError: No module named 'django.core.urlresolvers'

ImportError: No module named 'django.core.urlresolvers'


https://stackoverflow.com/questions/43139081/importerror-no-module-named-django-core-urlresolvers

from django.core.urlresolvers import reverse

to:

from django.urls import reverse


pinax error: no module named debug toolbar

pip install django-debug-toolbar

ImportError: No module named 'django_extensions'

pip install django-extensions


>>> import django
>>> django.get_version()
'1.6.1'


```
python manage.py makemigrations && python manage.py migrate
```

```
python manage.py createsuperuser
```