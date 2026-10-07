print("-----Basic Calculator-----")

num1 = float(input("Enter First Number: "))

operator = input("Enter Operator(+, -, *, /, %, //, **): ")

num2 = float(input("Enter Second Number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        result = "Cannot devided by zero"
    else:
        result = num1 // num2
elif operator == "%":
    result = num1 % num2
elif operator == "//":
    if num2 == 0:
        result = "Cannot devided by zero"
    else:
        result = num1 // num2
elif operator == "**":
    result = num1 ** num2
else:
    result = "invalid operator"
    
print("Result:", result)