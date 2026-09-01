class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return f"{self.name} scored {self.marks} marks"

Student = Student("Ravi", 86)

print(Student)