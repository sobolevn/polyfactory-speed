import datetime as dt

import pydantic

CITIES = ['Berlin', 'London', 'Madrid']

class MyUser(pydantic.BaseModel):
    id: int
    email: pydantic.EmailStr
    full_name: str
    age: int
    country: str
    city: str
    address: str
    subscription_starts: dt.datetime
    subscription_ends: dt.datetime
