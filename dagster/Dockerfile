FROM python:3.8-slim
MAINTAINER Nicolas Ramy <devops@darkelda.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV DAGSTER_HOME /app

RUN apt-get update \
    && apt-get upgrade \
    && apt-get install -y gcc \
                          python3-dev \
                          libpq-dev \
                          postgresql-client \
                          postgresql-client-common

RUN pip install --upgrade pip
RUN pip install dagster \
                dagster-dask \
                dagster-postgres \
                dagster-aws \
                dagit

RUN mkdir $DAGSTER_HOME
WORKDIR /$DAGSTER_HOME
COPY . $DAGSTER_HOME
RUN chmod +x $DAGSTER_HOME/entrypoint.sh

VOLUME ["$DAGSTER_HOME"]

EXPOSE 3000

ENTRYPOINT ["ash", "$DAGSTER_HOME/entrypoint.sh"]
