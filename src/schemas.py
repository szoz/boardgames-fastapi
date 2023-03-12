from pydantic import BaseModel


class SchemaModel(BaseModel):
    """Project-level base Pydantic model."""

    pass


class APIResponse(SchemaModel):
    """Generic API response model."""

    status: str
