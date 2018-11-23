FROM python:3.6-alpine3.7

ENV LANG C.UTF-8
ENV APP_ROOT /code
WORKDIR $APP_ROOT

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # Translations dependencies
  && apk add gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  #&& apk add libffi
  && apk add postgresql-client

###################### pip install
COPY Pipfile Pipfile.lock ./
ADD ./requirements requirements
RUN pip install -r requirements/local.txt
RUN pip install django-taggit
RUN pip install djangorestframework-jwt
RUN pip install django-taggit-serializer
##################################Supervisor install

#ENV SUPERVISOR_VERSION=3.3.1

RUN apk update && apk add py-pip python ;\
    apk add bash curl vim git tzdata shadow sudo

RUN pip install git+https://github.com/Supervisor/supervisor
ADD ./attachment /attachment

RUN cp -arp /attachment/supervisor/supervisord.d /etc/supervisord.d ;\
    cp -arp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime ;\
    cp -arp /attachment/supervisor/supervisord.conf /etc/supervisord.conf ;\
    cp -arp /attachment/cmd/ready.sh /ready.sh

CMD sh /ready.sh && /usr/local/bin/supervisord -c /etc/supervisord.conf