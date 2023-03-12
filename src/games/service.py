from typing import Type

from sqlalchemy.orm import Session

from src.games import models


def read_games(db: Session) -> list[Type[models.Game]]:
    """Return list of all games."""
    return db.query(models.Game).all()


def read_game(db: Session, _id: int) -> models.Game | None:
    """Return game based on given ID."""
    return db.query(models.Game).filter(models.Game.id == _id).first()
