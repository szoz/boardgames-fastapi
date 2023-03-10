from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Return simple response to indicate that server is running."""
    return {"status": "OK"}
