def numbers():
    for i in range(1, 101):
        yield i
for number in numbers():
    print(number)