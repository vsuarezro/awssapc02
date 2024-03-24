from typing import Dict, Optional

from fastapi import FastAPI, Response
from pydantic import BaseModel


class Food(BaseModel):
    """Model from Bite 02"""

    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: Optional[float] = 0.0


app = FastAPI()
foods: Dict[int, Food] = {}
data = {"id":1, "name":"egg", "serving_size":"piece", "kcal_per_serving": 78, "protein_grams": 6.3, "fibre_grams":0.0}
foods[1] = Food(**data)

@app.get("/", status_code = 405)
async def get_create_foods(response:Response):
    return {"message": "method GET not allowed"}

@app.post("/", response_model=Food, status_code=201)
async def create_foods(food: Food, response:Response):
    for _saved_food in foods.values():
        if food.name == _saved_food.name:
            foods[_saved_food.id] = food
            return food
    else:
        last_id = len(foods.keys())
        last_id += 1
    foods[last_id] = food
    return foods[last_id]
