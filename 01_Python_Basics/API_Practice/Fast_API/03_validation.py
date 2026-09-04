from fastapi import FastAPI
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(ge=1, le=100000)

app = FastAPI()

@app.post("/products")
def cerate_product(product:Product):
    return product