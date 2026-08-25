# Opening file
f = open("geek.txt", "r")
print(f)

print("==================")

# Closing file

file = open("geek.txt", "r")
file.close()

print("==================")
# Checking file properties

f = open("geek.txt", "r")
print("File_name:", f.name)
print("Mode:", f.mode)
print("Is closed?:", f.closed)
f.close()
print("Is closed?:", f.closed)

print("==================")

# Reading a file
file2 = open("geek.txt", "r")

content = file2.read()

print(content)

file2.close()

print("==================")

# Writing a file
with open("geek.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")
print("File written Successfully")

print("===================")

# Using with Statement
with open("geek.txt", "r") as file:
    content = file.read()
    print(content)

print("==================")

# Handling Exceptions When Closing a File
try:
    file = open("geek.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("Error:", e)
finally:
    file.close()