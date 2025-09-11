from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = 'John Smith'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

external_data = {
    'id': '123',
    'signup_ts': '2025-08-27 11:34',
    'friends': [1, 2, '3'],
}

user = User(**external_data)
print(user.id)
print(repr(user.signup_ts))
print(user.friends)
# print(user.dict())   # The `dict` method is deprecated in Pydantic V2.0
print(user.model_dump())  # Use `model_dump` instead

# Usage of ** & * in dict
def unpacking_and_packing_dict(**kwargs):
    for key, value in kwargs.items():
        print(f'Key is {key}, Value is {value}')  # Unpacking
    print(kwargs)  # Packing
    print(*kwargs)

print('===' * 10)
unpacking_and_packing_dict(a=1, b=2, c=3)
