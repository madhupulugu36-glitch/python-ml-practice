# Filter items out of a sequence
# Return filtered list

# Traditional Approach - filter even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = []

for num in numbers:
    if num % 2 ==0:
        result.append(num)
print(result)

print("=================")

# filter() + lambda Approach - filter even numbers

numbers = [11, 12, 13, 14, 15, 16, 17, 18]
result = list(filter(lambda num: num%2==0, numbers))
print(result)

print("=================")

# Traditional Approach - filter even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = []

for num in numbers:
    if num%2!=0:
        result.append(num)
print(result)

print("=============")

# filter() + lambda Approach - filter even numbers

numbers = [101, 102, 103, 104, 105, 106, 107, 108, 109]
result = list(filter(lambda num: num % 2 != 0, numbers))
print(result)

print("=================")

#Traditional Approach - Filter numbers greater than 10

numbers = [5, 11, 7, 14, 19, 4, 21]
result = []
for num in numbers:
    if num > 10:
        result.append(num)
print(result)

print("================")

#filter() + lambda Approach - Filter numbers greater than 10

numbers = [5, 11, 7, 14, 19, 4, 21]
result = list(filter(lambda num: num > 10, numbers))
print(result)

print("====================")

# Traditional Approach - Filter names starting with "A"

names = ["Alice", "Bob", "Anil", "David", "Arun"]
result = []
for name in names:
    if name.startswith("A"):
        result.append(name)
print(result)

print("==============")

# Traditional Approach - Filter names starting with "A"

names = ["Alice", "Bob", "Anil", "David", "Arun"]
result = list(filter(lambda name: name.startswith("A"), names))
print(result)