from fastapi import APIRouter
from typing import Union, Optional, List
from pydantic import BaseModel, Field, field_validator
from datetime import date

app03 = APIRouter()


class Addr(BaseModel):
    city: str
    street: str


class User(BaseModel):
    # Use regular expressions to validate user input
    # name: str = Field(default="root", pattern="^a")
    name: str = "root"
    age: int = Field(default=0, gt=0, lt=100)
    birth: Union[date, None] = None
    friends: List[int] = []
    description: Optional[str] = None
    addr: Addr

    @field_validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), "name must be alphabetic"
        return value


# object BaseModel can be nested
class Data(BaseModel):
    data: List[User]


@app03.post("/user")
async def post_user(user: User):
    print(user, type(user))
    print(user.name, user.birth)
    print(user.model_dump())        # .dict() in class "BaseModel" is deprecated, use .model_dump() instead
    return user


@app03.post("/data")
async def post_data(data: Data):
    return data
