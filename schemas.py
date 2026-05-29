# Schema:
from pydantic import BaseModel

class Emp(BaseModel):

    id: int
    name: str
    age: int


class User(BaseModel):

    username: str
    password: str


class UpdateEmp(BaseModel):

    name: str
    age: int