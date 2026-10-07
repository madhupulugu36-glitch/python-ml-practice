print("----- Function-Based Calculator -----")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def modulus(a, b):
    if b == 0:
        return "Cannot divide by Zero"
    return a % b


def floor_division(a, b):
    if b == 0:
        return "Cannot divide by Zero"
    return a // b


def power(a, b):
    return a ** b


while True:
    
    try:
        num1 = float(input("Enter First Number: "))
    except ValueError:
        print("Invalid input. Please enter a number: ")
        continue
    
    
    operator = input("Enter Operator (+, -, *, /, %, //, **): ")
    
    
    
    try:
        num2 = float(input("Enter Second Number: "))
    except ValueError:
        print("Invalid input. please enter a number: ")
        continue
    
    
    
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    elif operator == "%":
        result = modulus(num1, num2)
    elif operator == "//":
        result = floor_division(num1, num2)
    elif operator == "**":
        result = power(num1, num2)
    else:
        result = "Invalid Operator"
    
    print("Result:", result)
    
    
    while True:
        choice = input("Do you want to Continue? (Y/N): ")
        
        if choice.lower() == "y":
            break
        
        elif choice.lower() == "n":
            print("Calculator Closed.")
            exit()
        
        else:
            print("Please enter Y or N")