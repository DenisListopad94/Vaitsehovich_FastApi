from fastapi import FastAPI
from pydantic import BaseModel, PositiveInt, Field, constr
from enum import Enum


import random


app = FastAPI()


# Task 1,2
@app.get("/")
def random_five_num_list():
    numbers = []
    for i in range(5):
        numbers.append(random.randint(1, 100))
    return numbers


# Task 3
@app.get("/items/{item_id}")
def first_and_point(item_id: int):
    return {"item_id": item_id}


@app.get("/street/apartment_num")
def second_and_point(street: str, apartment_num: int) -> dict:
    return {"street": street,
            "apartment_num": apartment_num}


@app.get("/{person_id}/last_name/name")
def third_and_point(
        person_id: int,
        last_name: str,
        name: str
) -> dict:
    return {"person_id": person_id,
            "last_name": last_name,
            "name": name}


# Task 4,5
class GenderEnum(str, Enum):
    male = "male"
    female = "female"

class Actor(BaseModel):
    actor_id: PositiveInt
    name: constr(min_length=2, max_length=20)
    surname: constr(min_length=2, max_length=20)
    age: int = Field(gt=0, lt=100)
    sex: GenderEnum


@app.post("/actors")
def some_actors(actors: Actor) -> Actor:
    return actors