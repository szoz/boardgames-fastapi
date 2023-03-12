from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from src.database import get_db
from src.games import schemas, service

router = APIRouter()


@router.get("/games", response_model=list[schemas.Game])
def read_games_all(db: Session = Depends(get_db)):
    """Return list of all games."""
    return service.read_games(db)


@router.get("/games/{id}", response_model=schemas.Game)
def read_game(_id: int = Path(alias="id"), db: Session = Depends(get_db)):
    """Return list of all games."""
    if not (game := service.read_game(db, _id)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")
    return game
