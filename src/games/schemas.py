from pydantic import BaseModel, constr


class Game(BaseModel):
    id: int
    title: constr(max_length=100)
    year: int
    url: constr(max_length=100)
    description: str

    class Config:
        orm_mode = True
