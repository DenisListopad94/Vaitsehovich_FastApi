from fastapi import APIRouter
import random

router = APIRouter(
    prefix="",
    tags=["Booking"]
)

@router.get("/items")
def random_five_num_list():
    numbers = []
    for i in range(5):
        numbers.append(random.randint(1, 100))
    return numbers