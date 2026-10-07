from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Calculator API is runnning"}

@app.get("/add")
def add(
    num1: float = Query(..., ge=-1000000, le=1000000, description="First number"),
    num2: float = Query(..., ge=-1000000, le=1000000, description="Second number")
):
    result = num1 + num2
    
    return{
        "num1": num1,
        "num2": num2,
        "result": result
    }
    
@app.get("/subtract")
def subtract(num1: float, num2: float):
    result = num1 - num2
    
    return{
        "num1": num1,
        "num2": num2,
        "result": result
    }
    
@app.get("/multiply")
def multify(num1: float, num2: float):
    result = num1 * num2
    
    return {
        "num1": num1,
        "num2": num2,
        "result": result
    }
    
@app.get("/divide")
def divide(num1: float, num2: float):

    if num2 == 0:
        return {
            "error": "Cannot divide by zero"
        }

    result = num1 / num2

    return {
        "num1": num1,
        "num2": num2,
        "result": result
    }


@app.get("/modulus")
def modulus(num1: float, num2: float):
    
    if num2 == 0:
        return{
            "error": "Cannot divide by Zero"
        }
    result = num1 % num2
    
    return{
        "num1": num1,
        "num2": num2,
        "result": result
    }
    
@app.get("/floor")
def floor_division(num1: float, num2: float):
    
    if num2 == 0:
        return{
            "error": "Cannot divide by Zero"
        }
    
    result = num1 // num2
    
    return {
        "num1": num1,
        "num2": num2,
        "result": result
    }
    

@app.get("/power")
def power(num1: float, num2:float):
    result = num1 ** num2
    
    return{
        "num1": num1,
        "num2": num2,
        "result": result
    }