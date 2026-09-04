from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int =0
    email: str

app = FastAPI()

@app.post("/users")
def create_user(user: User):
    return user