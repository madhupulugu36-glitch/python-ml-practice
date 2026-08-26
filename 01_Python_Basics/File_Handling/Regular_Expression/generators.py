def numbers():
    yield 200
    yield 300
    yield 400
result = numbers()

print(next(result))
print(next(result))
print(next(result))