from fastapi import APIRouter
from pydantic import BaseModel, EmailStr, PositiveInt, Field


class User(BaseModel):
    id: PositiveInt
    age: int = Field(default=1, gt=0, lt=100)
    first_name: str = "User"
    second_name: str = "Userskiy"
    user_name: str = "username"
    sex: str = "mail or femail"
    email: EmailStr = "user@example.com"

router = APIRouter(
    prefix="/users",
    tags=["Authentication"]
)

@router.post("", response_model=User)
def get_user() -> User:
    user_db = {
        "id": 1,
        "age": 24,
        "name": "User",
        "surname": "Userskiy",
        "email": "user@example.com"
    }
    user = User(**user_db)
    return user


