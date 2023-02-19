import typing

import pytest
from httpx import AsyncClient

from src.entrypoints.http import app


@pytest.fixture(scope="session")
async def get_client() -> typing.AsyncGenerator:
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client
