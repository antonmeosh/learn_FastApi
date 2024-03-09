from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        Schema_extra = {"example": {"id": 1, "item": "Example schema"}}


class TodoItem(BaseModel):
    item: str

    class Config:
        Schema_extra = {"example": {"item": "Read the next chapter of the book"}}
