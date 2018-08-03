FROM python:3.6
MAINTAINER jeremy.harris@zenosmosis.com

RUN apt-get update \
  && apt-get install -y \
  libpq-dev \
  postgresql-client \
  postgresql-client-common \
  python3-psycopg2 \
  # Clean up apt-cache
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /src/*.deb 

# Install Python project dependencies
RUN pip install Flask SQLAlchemy psycopg2-binary phonenumbers

WORKDIR /app

ADD . /app

ENV FLASK_APP=backend/python/server.py

# Our seed data
# COPY data/interview-callerid-data.csv.gz /tmp/callerid.csv.gz
# RUN gzip -d /tmp/callerid.csv.gz

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]