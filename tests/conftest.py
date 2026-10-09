from collections.abc import AsyncIterator

import pytest
from httpx import ASGITransport, AsyncClient

from src.entrypoints.http import app


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client
