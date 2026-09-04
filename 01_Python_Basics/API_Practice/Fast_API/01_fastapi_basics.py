from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Madhu, FastAPI is Working!"}

@app.get("/about")
def about():
    return {"message": "This is my FastAPI About page"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/search")
def search(name: str = "Guest", age: int = 0):
    return {"name": name, "age": age}