FROM python:3.11 AS requirements
WORKDIR /app
COPY . /app
RUN ./scripts/generate-requirements.sh > ./unified_requirements.txt

FROM python:3.11

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install gettext -y

COPY --from=requirements /app/unified_requirements.txt /app/
RUN cat /app/unified_requirements.txt | pip install -r /dev/stdin;
RUN pip install psycopg2-binary;

COPY . /app

RUN python manage.py collectstatic --noinput

RUN useradd -m -u 1001 -s /bin/bash app
USER 1001

EXPOSE 8080

CMD ["/app/scripts/run-server.sh"]
