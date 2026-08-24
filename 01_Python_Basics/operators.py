#Arthimatic Operators
x = 25
y = 4

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)

print("-------------------")

#Relational Operators

a = 72
b = 64
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Less Than:", a < b)
print("Greater Than:", a > b)
print("Less Than or Equal:", a <= b)
print("Greater Than or Equal:", a >= b)

print("-------------------")

#Logical Operators
c = True
d = False
print("Logical AND:", c and d)
print("Logical OR:", c or d)
print("Logical NOT:", not c)
print("Logical NOT:", not d)

print("-------------------")

#Bitwise Operators

a = 20
b = 10
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Bitwise Left Shift:", a << 2)
print("Bitwise Right Shift:", a >> 2)

print("-------------------")

#Assignment Operators
x = 10
print("x =", x)
print("x += 5:", x + 5)
print("x -= 3:", x - 3)
print("x *= 2:", x * 2)
print("x /= 4:", x / 4)
print("x //= 3:", x // 3)
print("x %= 4:", x % 4)
print("x **= 2:", x ** 2)
print("x &= 3:", x & 3)
print("x |= 5:", x | 5)
print("x ^= 2:", x ^ 2)
print("x <<= 1:", x << 1)
print("x >>= 2:", x >> 2)


print("-------------------")

#ternary Operator
age = 18
status = "Adult" if age >= 18 else "Not Adult"
print("Status:", status)


a = 10
b = 20
c = a if a < b else b
print("minimum value:", c)

print("-------------------")

#Identity Operators
a = student = {"name": "John", "age": 19, "status": "Passed"}
print("Identity Operator (is):", a is student)
print("Identity Operator (is not):", a is not student)

print("-------------------")

#Membership Operators

a = "Python"
b = "Java"
c = "SQL"
my_list = ["Python", "Java", "C++", "JavaScript"]

if a not in my_list:
    print("a is not present in given my_list:", a)
else:
    print("a is present in given my_list:", a)
if b not in my_list:
    print("b is not present in given my_list:", b)
else:
    print("b is present in given my_list:", b)
if c not in my_list:
    print("c is not present in given my_list:", c)
else:
    print("c is present in given my_list:", c)
