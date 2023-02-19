dev.local:
	docker-compose -f docker-compose-local.yml up -d && uvicorn src.entrypoints.api:app --reload

database.migration:
	alembic revision --autogenerate

database.upgrade:
	alembic upgrade head

database.downgrade:
	alembic downgrade -1
