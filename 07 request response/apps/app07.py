from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from typing import Union

app07 = APIRouter()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 42.0},
    "bar": {"name": "Bar", "description": "A bar item", "price": 24.0, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": None,
        "price": 50.2,
        "tax": 5,
        "tags": ["bar"],
    },
}


@app07.post("/user02", response_model=UserOut)
def create_user(user: UserIn):
    return user


# response_model_exclude_unset=True,            # Excludes fields values that were not explicitly set
# response_model_exclude_defaults=True,         # Excludes fields that have their default values
# response_model_exclude_none=True,             # Excludes fields with None values
# response_model_include={"name", "price"},     # Only includes the specified fields
# response_model_exclude={"description"}        # Excludes the specified fields
@app07.get("/items/{item_id}", response_model=Item, response_model_include={"name", "price"})
async def read_item(item_id: str):
    return items[item_id]
