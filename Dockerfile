FROM python:3.11

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install gettext -y

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install psycopg2-binary --force-reinstall --no-cache-dir;

COPY . /app

RUN find . -name "requirements.txt" -print0 | xargs -0 -n1 pip install --upgrade -r;

EXPOSE 8000

CMD ["/app/scripts/run-server.sh"]
