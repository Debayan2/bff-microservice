from pydantic import BaseModel # type: ignore

class UserProfile(BaseModel):
    id: int
    name: str
    email: str

class Product(BaseModel):
    id: int
    name: str
    price: float
