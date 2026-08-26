#open the file in read mode
file = open("example1.txt", "r")

#Read the entire content of the file
content = file.read()
print(content)

#close the file
file.close()

file = open("example2.txt", "r")
for line in file:
    print(line.strip())

file.close()