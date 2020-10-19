FROM python:3.8-alpine
MAINTAINER Nicolas Ramy <devops@darkelda.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV DAGSTER_HOME /app

# Extra repositories
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

RUN apk update \
    && apk upgrade \
    && apk add build-base linux-headers \
                          gcc python3-dev \
                          musl-dev \
                          make \
    && apk add jpeg-dev \
               zlib-dev \
               freetype-dev \
               lcms2-dev \
               openjpeg-dev \
               tiff-dev \
               tk-dev \
               tcl-dev \
               harfbuzz-dev \
               fribidi-dev\
               postgresql-dev \
               openssl-dev \
               libffi-dev \
               git

RUN pip install --upgrade pip
RUN pip install dagster \
                dagster-dask \
                dagster-postgres \
                dagit

RUN mkdir /app
WORKDIR /app
COPY . /app

VOLUME ["/app"]

CMD ["dagit", "-h", "0.0.0.0", "-p", "3000"]
