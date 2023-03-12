from contextlib import contextmanager

import pytest
from fastapi.testclient import TestClient

from src.database import Base, engine, get_db
from src.games import models
from src.main import app

sample_games = [
    {
        "id": 162886,
        "title": "Spirit Island",
        "year": 2017,
        "url": "https://boardgamegeek.com/boardgame/162886/spirit-island",
        "description": "Island Spirits join forces using elemental powers to defend their home from invaders.",
    },
    {
        "id": 220308,
        "title": "Gaia Project",
        "year": 2017,
        "url": "https://boardgamegeek.com/boardgame/220308/gaia-project",
        "description": "Expand, research, upgrade, and settle the galaxy with one of 14 alien species.",
    },
    {
        "id": 316554,
        "title": "Dune: Imperium",
        "year": 2020,
        "url": "https://boardgamegeek.com/boardgame/316554/dune-imperium",
        "description": "Influence, intrigue, and combat in the universe of Dune.",
    },
]


@pytest.fixture(scope="session")
def db_setup() -> None:
    """Creates game column in database and fills it with sample data."""
    Base.metadata.create_all(bind=engine)
    with contextmanager(get_db)() as db:
        for game in sample_games:
            if not db.query(models.Game.id == game["id"]).first():
                db.add(models.Game(**game))
        db.commit()


@pytest.fixture(scope="session")
def client(db_setup) -> TestClient:
    """Return FastAPI test client."""
    return TestClient(app)
