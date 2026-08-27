# Apply same function to each element od a sequence
# Return the modified list

# traditional Approach - DOuble every number

numbers = [1, 2, 3, 4, 5]

result = []

for num in numbers:
    result.append(num * 2)

print(result)

print("================")

# map() + lambda Approach - DOuble every number

numbers = [10, 20, 30, 40, 50]

result = list(map(lambda num: num * 2, numbers))

print(result)

print("================")

# Traditional Approach - Add two list numbers

a = [10, 20, 30, 40, 50]

b = [11, 12, 13, 14, 15]

result = []

for x, y in zip(a, b):
    result.append(x + y)

print(result)

print("==============")

# map() + lambda Approch - Add two list numbers

a = [1, 11, 21, 31, 41]
b = [49, 39, 29, 19, 9]

result = list(map(lambda x, y: x + y, a, b))

print(result)

print("==================")

# Tradition Approach- Find maximum between two lists

a = [101, 89, 107, 109, 97]
b = [98, 103, 79, 118, 106]

result = []

for x, y in zip(a,b):
    if x>y:
        result.append(x)
    else:
        result.append(y)
print(result)

print("================")

# map() + lambda Approach - Find maximum between two lists

a = [101, 89, 107, 109, 97]
b = [98, 103, 79, 118, 106]

result = list(map(lambda x, y: x if x>y else y, a, b))

print(result)