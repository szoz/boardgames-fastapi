from fastapi import FastAPI

from src.games.router import router as games_router

app = FastAPI()

app.include_router(games_router, tags=["games"])


@app.get("/")
async def root():
    """Return simple response to indicate that server is running."""
    return {"status": "OK"}
