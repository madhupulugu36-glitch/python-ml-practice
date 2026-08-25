# Read Mode ('r')
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
print("===============")

#Write Mode ('w')
with open("example.txt", "w") as file:
    file.write("Hello, world!")