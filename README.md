# FastAPI Template

## Directory explanation:

```bash
├── config
├── migrations
│   └── versions
├── src
│   ├── entrypoints
│   ├── models
│   ├── routes
│   └── services
│   └── repositories
└── tests

```

### config:

This folder is responsible to save
configuration files like project constants
or environment variables .

```bash
├── config
│   ├── conts.py
│   └── envs.py

```

### migrations:

Alembic's migrations directory.

```bash
├── migrations
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│   └── 3034f17c14fe_.py

```

### src:

Project source code.

```bash
├── src
│   ├── entrypoints
│   ├── models
│   ├── routes
│   └── services
│   └── repositories

```

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

Base code tests.

```bash
└── tests
└── conftest.py

```
