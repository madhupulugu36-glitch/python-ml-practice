# reduce() is used for when we want to combine multiple values into one final value.
# Applies same operation to items of a sequence.
# Uses return of operation as first parameter of nexy operation.
# Returns an item, not a list.

# Traditional Approach - Sum of all numbers.

numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total=total+num

print(total)

print("============")

# reduce() + lambda Approach - Sum of all numbers.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x+y, numbers)
print(result)

print("==============")

# Traditional Approch - Production of all numbers.

numbers = [1, 2, 3, 4, 5]

result = 1

for num in numbers:
    result = result * num
print(result)

print("===========")

# reduce() + lambda Approch - Production of all numbers.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x,y: x*y, numbers)
print(result)

print("==========")

# Traditional Approch Maximum number from a list.

numbers = [10, 25, 8, 40, 15]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
print(maximum)

print("=============")

# reduce() + lambda Approch - Maximum number from a list.

from functools import reduce

numbers = [10, 25, 8, 40, 15]

result = reduce(lambda x, y: x if x > y else y, numbers)

print(result)