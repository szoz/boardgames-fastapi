from pydantic import constr

from src.schemas import SchemaModel


class Game(SchemaModel):
    id: int
    title: constr(max_length=100)
    year: int
    url: constr(max_length=100)
    description: str

    class Config:
        orm_mode = True
