print("------variables------")
name = "Sai"
age = 20
is_student = True

print("------f-String------")
#f-String
print(f"{name} is {age} years of old")

print("------Multiple Assignment------")
#Multiple Assignment
x, y, z = 25, 35, 45
print("Values of x, y, z:", x, y, z)


#Swapping of values
print("------Swapping of Values------")
a, b =15, 25
print("Before:", a, b)
a,b = b,a
print("After:", a, b)

a, b, c, d = 5, 10, 15, 20
print("Before:", a, b, c, d)
a, b, c, d = d, c, b, a
print("After:", a, b, c, d)

print("------List Comprehension------")
#List Comprehension
squares = [x*x for x in range(1, 12)]
print("Squares:", squares)

print("------enumerate()------")
#enumerate()
items = ["laptop", "mobile", "desktop"]
for i, value in enumerate(items):
    print(f"Index: {i}, Value: {value}")


#zip
print("------zip------")
names = ["John", "daniel", "david"]
roles = ["Qa", "Dev", "Ml Engineer"]

for name, role in zip(names, roles):
    print(f"Name: {name}, Role: {role}")
    
#Use built-in functions
print("------Built-in Functions------")
numbers = [1, 7, 2, 9, 3, 11, 4, 5]
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))
print("Reversed:", list(reversed(numbers)))
print("Descending order:", sorted(numbers, reverse=True))

#use "in" for multiple conditions
print("------Use 'in' for multiple conditions------")
name = "john"
if name in ["john", "david", "daniel"]:
    print(f"Name: {name} found")

#Use any() and all()
print("------Use any() and all()------")
numbers = [10, 201, 20, 372, 11]
if any(x > 200 for x in numbers):
    print("Found large numbers")

if all(x > 9 for x in numbers):
    print("All numbers are greater than 9")



#Ternary Operator (Short if-else)
print("------Ternary Operator (Short if-else)------")
marks = 150
result = "Pass" if marks >= 40 else "fail"
print(f"{marks} {result}")

#Use Dictionary for multiple Actions
print("------Use Dictionary for multiple Actions------")
def add():
    print("Addition")
def delete():
    print("Deletion")
def update():
    print("Updation")
    
actions = {
    "add": add,
    "delete": delete,
    "update": update
}
choice = "delete"
actions[choice]()  # Call the function based on the choice

#Efficient use of range()
print("------Efficient use of range()------")
for i in range(10):
    print(i)
print("Even numbers from 2 to 10:")
for i in range(2, 11, 2):
    print(i)
    
#Use enumerate()
print("------Use enumerate()------")
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)
    
#Use zip()
print("------Use zip()------")
names = ["John", "Daniel", "David"]
roles = ["QA", "Dev", "ML Engineer"]
for name, role in zip(names, roles):
    print(name, "=>", role)
    
#Loop Tricks: Break, Continue, Pass
print("------Loop Tricks: Break, Continue, Pass------")
for n in range(10):
    if n == 5:
        continue  # Skip the rest of the loop for n=5
    if n ==8:
        break  # Exit the loop when n=8
    if n ==3:
        pass # Do nothing for n=3
    print(n)
    
#Reverse a loop / iterate backwards
print("------Reverse a loop / iterate backwards------")
numbers = [5, 15, 25, 35, 45]
for n in reversed(numbers):
    print(n)
    
#Nested Loops(Quick patterns)
print("------Nested Loops(Quick patterns)------")
for i in range(3):
    for j in range(3):
        print(i, j)


#List Tricks
print("------List Tricks------")
nums = [10, 20, 30, 40, 50]
print(nums)
nums.append(60)  # Add an element to the end of the list
print("Append-60:", nums)
nums.remove(20)  # Remove the first occurrence of 20
print("Remove-20:", nums)
nums.insert(1, 15) # Insert 15 at index 1
print("Insert-15 at index 1:", nums)
nums.pop()  # Remove and return the last element
print("Pop:", nums)
nums.sort()  # Sort the list in ascending order
print("Sort (ascending):", nums)
nums.sort(reverse=True) # Sort the list in descending order
print("Sort (descending):", nums)
new_list = sorted(nums)  # Create a new sorted list without modifying the original
print("New sorted list:", new_list)
unique = list(set(nums))  # Get unique elements from the list and remove duplicates
print("Unique elements:", unique)
print("Length of the list:", len(nums))

#List Comprehension (Fast and Clean)
print("------List Comprehension (Fast and Clean)------")
print("-----Squares of numbers-----")
squares = [x*x for x in range(11)]
print("Squares:", squares)

#Even numbers using list comprehension
print("-----Even numbers-----")
evens = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", evens)

#Odd numbers using list comprehension
print("-----Odd numbers-----")
odds = [x for x in range(20) if x % 2 != 0]
print("Odd numbers:", odds)

#from existing list
print("-----From existing list-----")
nums = [1, 2, 3, 4]
doubled = [x*2 for x in nums]
print("Doubled:", doubled)


#String Tricks (Common Operations)
print("------String Tricks (Common Operations)------")
text = "  Hello Python  "
print("Stripped:", text.strip())  # Remove leading and trailing whitespace
print("Uppercase:", text.upper())  # Convert to uppercase
print("Lowercase:", text.lower()) # Convert to lowercase
print("Replaced:", text.replace("o", "0"))  # Replace 'o' with '0'

words = text.split() # Split the string into a list of words

result = "-".join(words)  # Join the list of words with a hyphen

print(text[::-1])  # Reverse the string

#Dictionary Tricks
print("------Dictionary Tricks------")
data = {"name": "John", "age": 30, "role": "ML Engineer"}
print(data["name"])  # Access value by key
print(data.get("age"))  # Access value by key using get()
print(data.get("city", "N/A"))  # Access value by key with default if key doesn't exist
data["city"] = "Hyderabad"  # Add a new key-value pair
for key, value in data.items():  # Iterate through dictionary items
    print(key, value)

data.pop("age")  # Remove a key-value pair
print("name" in data)  # Check if a key exists

#Tuple Tricks
print("------Tuple Tricks------")
point = (10, 20)
x, y = point  # Unpack tuple
print("X:", x, "Y:", y)
single = (5,)  # Single element tuple
nums = (1, 2, 3, 4)
print(2 in nums)  # Check if an element exists
print(len(nums))  # Length of the tuple

#Set Tricks
print("------Set Tricks------")
nums = [1, 2, 2, 3, 3, 4]
unique = set(nums)  # Create a set from a list
print("Unique elements:", unique)

a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)  # Union of sets
print("Intersection:", a & b)  # Intersection of sets
print("Difference:", a - b)  # Difference of sets
print("Symmetric Difference:", a ^ b)  # Symmetric difference of sets

#Slicing Tricks
print("------Slicing Tricks------")
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[1:4])  # Slice from index 1 to 3
print(nums[:3])  # Slice from start to index 2
print(nums[3:])  # Slice from index 3 to end
print(nums[-3:])  # Slice last 3 elements
print(nums[::-1])  # Reverse the list
print(nums[::2])  # Slice every second element

text = "python"
print(text[1:4]) 
print(text[::-1])  # Reverse the string

#Unpacking & multiple Assignment
print("------Unpacking & multiple Assignment------")
a, b = 10, 20 # Assign values to multiple variables
a, b = b, a # Swap values
x, *rest = [1, 2, 3, 4, 5] # Unpack list into variables
print("x:", x)
print("rest:", rest)

name, age, city = ("John", 30, "New York") # Unpack tuple into variables
print(name, age, city)

#Debugging Trick (Find Errors Fast)
print("-----Debugging Trick------")
x = 10
y = "20"
print(type(x))
print(type(y))

print(f" x= {x}, y = {y}") #Debugging values
assert x > 0, "x must be positive"  # Assertion

#Handle Errors Gracefully
print("-----Handle Errors Gracefully------")
try:
    a = int(input("Enter a number: "))
    print(100/a)
except ZeroDivisionError:
    print("Cannot devided by Zero!")
except ValueError:
    print("Enter Valid Number")
except Exception as e:
    print(f"Error: {e}")

#Use Functions
print("-----Use Functions------")
def add(a, b):
    return a + b
def greet(name="user"):
    return f"Hello {name}!"

print(add(4, 6))
print(greet())
print(greet("John"))

#Use lambda functions (for small tasks)
print("----Lambda functions----")
#Normal functions
def square(x):
    return x * x
#Lambda function
square = lambda x: x * x
print(square(6))

#use with Sorted
nums = [(1, 3), (2, 1), (3, 2)]
nums.sort(key=lambda x: x[1])
print(nums)

#Use Built-in Functions
numbers1 = [5, 4, 9, 3, 7]
print(len(numbers1))
print(sum(numbers1))
print(max(numbers1))
print(min(numbers1))
print(sorted(numbers1))
print(sorted(numbers1, reverse=True))

#Model Imports (Work Faster)
print("----Model Imports-----")
import math
import random
from collections import Counter, defaultdict
import itertools
import datetime

print(math.sqrt(5))
print(random.randint(1, 10))
print(Counter([1, 2, 2, 3]))
print(datetime.datetime.now())

#