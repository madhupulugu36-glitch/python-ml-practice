"""# Read Mode ('r')
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
print("===============")

#Read and Write Mode ('r+')
with open("example.txt", "r+") as file:
    content = file.read()
    file.write("\nThis is a read and write mode(r+)")
    file.write("\nletitbex AI")

print("===============")

#Write Mode ('w')
with open("example.txt", "w") as file:
    file.write("Hello, world!")

print("============")

#Write Mode ('w')
with open("example1.txt", "w") as file:
    file.write("Hello, world!")

print("=================")"""

#Write and Read Mode ('w+')
with open("example.txt", "w+") as file:
    file.write("Welcom to Python!")
    file.seek(0)
    content = file.read()

"""# Append Mode ('a')
with open("example1.txt", "a") as file:
    file.write("\nThis is a new line.")

print("================")

# Binary Mode ('b')
with open("image.png", "rb") as file:
    data = file.read()"""
