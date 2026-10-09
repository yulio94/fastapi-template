dev:
	docker compose up -d db && uv run uvicorn src.entrypoints.http:app --reload

db.migration:
	uv run alembic revision --autogenerate -m "$(m)"

db.upgrade:
	uv run alembic upgrade head

db.downgrade:
	uv run alembic downgrade -1

test:
	uv run pytest

lint:
	uv run pre-commit run --all-files
