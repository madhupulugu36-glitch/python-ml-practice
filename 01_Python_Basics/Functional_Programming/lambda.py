# Lambda
# A simple one line function
# Do not use def or return keywords
# These are implicit in the function

# Traditional way - double X

def double(X):
    return X * 2
print(double(3))

print("======================")

# Lambda function - double X

double = lambda x: x*2
print(double(5))

print("======================")

# Traditional - add two numbers

def add(a, b):
    return a + b
print(add(10, 20))

print("======================")

# lambda function - add two numbers

add = lambda A, B: A + B
print(add(20, 30))

print("======================")

# tradition - find max number

def max(i, j):
    if i > j:
        return i
    else:
        return j
print(max(102, 201))

print("======================")

# Lambda function - find max

maximum = lambda I, J:I if I > J else J

print(maximum(234, 432))

print("======================")

# Traditional Approach

def double(num):

    return num*2


def add(a,b):

    return a+b

def maximum(a, b):
    if a>b:
        return a
    else:
        return b

print(double(10))

print(add(10,20))

print(maximum(123,321))

print("======================")

# Lambda Approach

double = lambda num:num*2

add = lambda x,y:x+y

maximum = lambda i,j: i if i>j else j

print(double(144))

print(add(101, 201))

print(maximum(9999, 999999))