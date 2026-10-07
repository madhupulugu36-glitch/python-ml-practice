print("----- Clean Function-Based Calculator -----")

#Addition
def add(a, b):
    return a + b

#Subtraction
def subtract(a, b):
    return a - b

#Multiplication
def multiply(a, b):
    return a * b

#Division
def divide(a, b):
    if b == 0:
        return "Cannot divide by Zero"
    return a / b

#Modulus
def modulus(a, b):
    if b == 0:
        return "Cannot divide by Zero"
    return a % b

#Floor division
def floor_division(a, b):
    if b == 0:
        return "cannot divide by Zero"
    return a // b

#Power
def power(a, b):
    return a ** b


#Get a valid number
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter valid number: ")


#Get a valid Operator
def get_operator():
    valid_operators = ["+", "-", "*", "/", "%", "//", "**"]
    
    while True:
        operator = input(
            "Enter operator (+, -, *, /, %, //, **): "
        )
        if operator in valid_operators:
            return operator
        print("Invalid operator. Please try again.")
        
#Perform Calculation
def calculate(num1, operator, num2):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)
    elif operator == "%":
        return modulus(num1, num2)
    elif operator == "//":
        return floor_division(num1, num2)
    elif operator == "**":
        return power(num1, num2)
    


# Main Calculator Loop
while True:
    
    num1 = get_number("Enter First Number: ")
    
    operator = get_operator()
    
    num2 = get_number("Enter Second Number: ")
    
    result = calculate(num1, operator, num2)
    
    print("Result:", result)
    
    
    # Continue / Exit validatio
    while True:
        
        choice = input("Do you want to continue? (Y/N): ")
        
        if choice.lower() == "y":
            break
        
        elif choice.lower() == "n":
            print("Calculator Closed.")
            exit()
        else:
            print("Please enter Y or N.")