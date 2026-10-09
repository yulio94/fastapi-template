"""App definition"""

from fastapi import FastAPI

from src.routes import health

app = FastAPI()
app.include_router(health.router)
