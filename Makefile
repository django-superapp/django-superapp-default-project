SHELL := /bin/bash
ifneq ("$(wildcard .env.local)","")
include .env.local
export $(shell sed 's/=.*//' .env.local)

# Update PATH variable
PATH := $(shell sed -n 's/^PATH=//p' .env.local):$(PATH):/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin
endif

venv: venv/touchfile

venv/touchfile: requirements.txt
	test -d venv || virtualenv venv
	touch venv/touchfile

install-requirements: venv/touchfile
	. venv/bin/activate && ./scripts/generate-requirements.sh | pip install --upgrade -r /dev/stdin
	. venv/bin/activate && pip install psycopg2-binary --force-reinstall --no-cache-dir; \
	cd superapp/apps/admin_portal/tailwind && npm install

setup-sample-env:
	cp .env.local.example .env.local;
	cp .env.example .env;


start-docker:
	docker-compose up -d --build

stop-docker:
	docker-compose stop

destroy-docker:
	docker-compose stop
	docker-compose down -v

migrate:
	python3 manage.py migrate

makemigrations:
	python3 manage.py makemigrations

createsuperuser:
	python3 manage.py createsuperuser

collectstatic:
	python3 manage.py collectstatic --no-input

start-tailwind-watch:
	cd superapp/apps/admin_portal/tailwind; \
	npm run tailwind:watch


makemessages:
	mkdir -p site-packages
	ln -s /usr/local/lib/python33.11/site-packages/unfold site-packages/unfold
	ln -s /usr/local/lib/python33.11/site-packages/django site-packages/django
	python3 manage.py makemessages -l de -l en -i venv -s
	rm -r site-packages

compilemessages:
	python3 manage.py compilemessages


create-fixtures:
	python3 manage.py dumpdata --natural-foreign --natural-primary --indent 2 --output fixtures/initial_data.json

load-fixtures:
	python3 manage.py loaddata fixtures/initial_data.json
