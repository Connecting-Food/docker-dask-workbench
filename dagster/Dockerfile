FROM python:3.8-alpine
MAINTAINER Nicolas Ramy <devops@darkelda.com>

ENV PYTHONDONTWRITEBYTECODE 1

# Extra repositories
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

RUN apk update && apk upgrade \
    && apk add --virtual build-deps gcc python3-dev musl-dev make \
    && apk add openssl-dev libffi-dev git

RUN pip install --upgrade pip
RUN pip install dagster dagit

CMD ["dagit"]
