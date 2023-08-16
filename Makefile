#!make
-include .env

makemigrations:
	poetry run alembic revision --autogenerate

migrate:
	poetry run alembic -x data=true upgrade head

start:
	make start-local-service
	make migrate
	poetry run python -m uvicorn app.main:app --reload

start-local-service:
	docker-compose -f ./local.yaml up db -d
