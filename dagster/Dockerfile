FROM python:3.8-slim
LABEL maintainer="nicolas.ramy@connecting-food.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV DAGSTER_HOME /dagster
ENV DAGSTER_VERSION 0.9.15

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
                    gcc \
                    python3-dev \
                    libpq-dev \
                    postgresql-client \
                    postgresql-client-common \
    && rm -rf /var/lib/apt/lists/*

RUN pip install dagster==${DAGSTER_VERSION} \
                dagster-dask==${DAGSTER_VERSION} \
                dagster-postgres==${DAGSTER_VERSION} \
                dagster-aws==${DAGSTER_VERSION} \
                dagit==${DAGSTER_VERSION}

RUN mkdir /dagster
WORKDIR /dagster
COPY . /dagster

VOLUME ["/dagster"]
EXPOSE 3000

CMD ["dagit", "-h", "0.0.0.0", "-p", "3000"]
