class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"student('{self.name}', {self.marks})"
student = Student("madhu", 78)
print(repr(student))