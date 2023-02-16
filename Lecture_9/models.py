from pydantic import BaseModel

class Person(BaseModel):
    id: int
    name: str
    age: int
    favourite_book_id: int = None

    