print("----f-String----")
name = "jhon"
age = 20
role = "Ml Engineer"
print(f"Employee Name: {name}, and Employee Age: {age}, and Employee Role: {role}")

print("----Multiple Assignment and Swapping----")
a, b, c, d = 5, 10, 15, 20
print("Before:", a, b, c, d)
a, b, c, d = d, c, b, a
print("After:", a, b, c, d)

print("----List Comprehension----")
qubes = [x*x*x for x in range(1, 10)]
print("Qubes:", qubes)

print("----enumerate()----")
milk_products = ["Curd", "Butter", "Cheese"]
for i, value in enumerate(milk_products):
    print(f"Index: {i}, value: {value}")
    
print("----zip()----")
animals = ["Tiger", "Deer", "Elephant"]
categories = ["Carnivore", "Herbivore", "Herbivore"]
for animal, category in zip(animals, categories):
    print(f"Animal:{animal}, Category: {category}")

