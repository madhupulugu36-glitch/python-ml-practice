from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

# Create database connection
engine = create_engine("sqlite:///students.db")

# Create a bass class
Base = declarative_base()

# Create Student model
class Student(Base):
    __tablename__ = "Students"


    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    course = Column(String)

print("Student ORM model created successfully!")


# Create the Students table in the database
Base.metadata.create_all(engine)
print("Students table created successfully!")

# Create a database session
#with Session(engine) as session:
    # Create a student object
   # student = Student(
 #       id = 106,
  #      name = "Kiran",
   #     age = 26,
    #    course = "Python"
    #)

    # Add student to session
    #session.add(student)

    # Save to database
    #session.commit()

#print("Student data inserted successfully!")

# Read student data using ORM
with Session(engine) as session:
    student = session.query(Student).filter_by(name="Kiran").first()

    print("\nStudent details:")

    print("ID:", student.id)
    print("Name:", student.name)
    print("Age:", student.age)
    print("Course:", student.course)

# Update student data using ORM
with Session(engine) as session:
    student = session.query(Student).filter_by(id=106).first()
    student.age = 27
    session.commit()
print("\nStudent data updated successfully!")

# verify the updated student data
with Session(engine) as session:
    student = session.query(Student).filter_by(id=106).first()

    print("\nUpdated Student:")
    print("ID:", student.id)
    print("Name:", student.name)
    print("Age:", student.age)
    print("Course:", student.course)

# Delete student using ORM
with Session(engine) as session:

    student = session.query(Student).filter_by(id=106).first()

    if student:
        session.delete(student)
        session.commit()
        print("\nStudent deleted successfully!")
    else:
        print("\nStudent not found!")


# Verify deletion
with Session(engine) as session:

    student = session.query(Student).filter_by(id=106).first()

    if student:
        print("Student still exists:", student.name)
    else:
        print("Student 106 does not exist!")

# Add Multiple students using ORM
with Session(engine) as session:
    students = [
        Student(id=201, name = "Arjun", age = 22, course = "Jva"),
        Student(id=202, name = "Meena", age = 25, course = "Python"),
        Student(id=203, name = "Ravi", age = 22, course = "Python"),
        Student(id=204, name = "Anita", age = 27, course = "Machine Learning"),
        Student(id=205, name = "Suresh", age = 24, course = "SQL")
    ]

    session.add_all(students)
    session.commit()

    print("\n5 students inserted successfully!")