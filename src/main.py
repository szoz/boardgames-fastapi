from fastapi import FastAPI

from src import schemas
from src.games.router import router as games_router

app = FastAPI()

app.include_router(games_router, tags=["games"])


@app.get("/", response_model=schemas.APIResponse, tags=["general"])
async def root():
    """Return simple response to indicate that server is running."""
    return {"status": "OK"}
