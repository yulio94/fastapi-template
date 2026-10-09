# FastAPI Template

## Setup

```bash
uv sync
cp env.example .env
make dev          # starts Postgres on :9991 and the API on :8000
make db.upgrade   # apply migrations
```

Other targets:

```bash
make db.migration m="add orders"   # autogenerate a revision
make db.downgrade
make test
make lint                          # ruff + mypy via pre-commit
```

Run `uv run pre-commit install` once to lint on every commit.

## Directory explanation:

```bash
├── config
├── migrations
│   └── versions
├── src
│   ├── entrypoints
│   ├── models
│   ├── repositories
│   ├── routes
│   └── services
└── tests
```

### config:

Settings loaded from environment variables and `.env`, see `config/settings.py`.
Add new variables as fields on `Settings`; the app fails at startup if a required one is missing.

### migrations:

Alembic's migrations directory. Revisions are named `YYYY_MM_DD_HHMM-<rev>_<slug>.py`.

### src:

Project source code.

#### entrypoints:

This directory is to split possible
entrypoints to your application; i.e. http, cli, etc.

#### models:

Save sqlalchemy models.

#### routes:

FastAPI routes and dependencies, also you can add directories for versioning your API.

#### services:

Save files for handle interaction between routes and repositories.

#### repositories:

Save repositories that interact with models and the database.

### tests:

Async tests use anyio's pytest plugin; mark them with `@pytest.mark.anyio` and use the `client` fixture from `conftest.py`.
