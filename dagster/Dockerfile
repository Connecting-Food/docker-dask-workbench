FROM python:3.8-slim
MAINTAINER Nicolas Ramy <devops@darkelda.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV DAGSTER_HOME /dagster

RUN apt-get update \
    && apt-get install -y gcc \
                          python3-dev \
                          libpq-dev \
                          postgresql-client \
                          postgresql-client-common \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install dagster \
                dagster-dask \
                dagster-postgres \
                dagster-aws \
                dagit

RUN mkdir /dagster
WORKDIR /dagster
COPY . /dagster

VOLUME ["/dagster"]
EXPOSE 3000

CMD ["dagit", "-h", "0.0.0.0", "-p", "3000"]
