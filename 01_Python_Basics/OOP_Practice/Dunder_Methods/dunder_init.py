class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("raghu", 24)

print(student.name)
print(student.age)

class Runner:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

Runner = Runner("Mahesh", "5km")

print(Runner.name)
print(Runner.distance)