from typing import List

from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: int = Field(..., gt=0, title="Todo ID")
    item: str = Field(..., title="Todo Item", max_length=100)

    class Config:
        schema_extra = {"example": {"id": 1, "item": "Example schema!"}}


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {"example": {"item": "Read the next chapter of the book"}}


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {"todos": [{"item": "Example schema 1!"}, {"item": "Example schema 2!"}]}
        }
