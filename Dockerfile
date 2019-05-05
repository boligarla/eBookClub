FROM python:3.7
MAINTAINER Ndeye Senghor App final csci-29 Project

ARG CI_USER_TOKEN
RUN echo "machine github.com\n  login $CI_USER_TOKEN\n" >~/.netrc


ENV PYTHONUNBUFFERED =1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_SRC=/src \
    PIPENV_HIDE_EMOJIS=true \
    PIPENV_COLORBLIND=true \
    PIPENV_NOSPIN=true


COPY ./requirements.txt /requirements.txt
#RUN apk add --update --no-cache postgresql-client jpeg-dev
#RUN apk add --update --no-cache --virtual .tmp-build-deps \
#      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
#RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app
#
#RUN mkdir -p /vol/web/media
#RUN mkdir -p /vol/web/static
#RUN adduser -D user
#RUN chown -R user:user /vol/
#RUN chmod -R 755 /vol/web
#USER user
