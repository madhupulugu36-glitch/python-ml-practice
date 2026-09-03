from sqlalchemy import create_engine, text

# Create SQLite Database
engine = create_engine("sqlite:///students.db")
print("Database engine created successfully!")

# Create Student table

with engine.connect() as connection:
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            course TEXT
        )
    """))
    connection.commit()

print("Students table created successfully!")   

# Insert student data into the Students table

#with engine.connect() as connection:
 #   connection.execute(text("""
  #      INSERT INTO Students (id, name, age, course)
   #     VALUES
    #    (101, 'Ravi', 23, 'Python'),
     #   (102, 'Priya', 21, 'Java'),
      #  (103, 'Amit', 22, 'C++'),
       # (104, 'Sneha', 24, 'JavaScript'),
        #(105, 'Rahul', 25, 'Data Science')

  #  """))
   # connection.commit()

print("Student data inserted successfully!")

# Select Student data from the Students table

with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM Students"))

    print("\nStudents Records:")

    for row in result:
        print(row)

# Select students studying Python from the Students table

with engine.connect() as connection:
    result = connection.execute(text("""
        SELECT * FROM Students
        WHERE course = 'Python'"""))
    print("\nStudents studying Python:")

    for row in result:
        print(row)

# Select students older than 22 from the Students table
with engine.connect() as connection:
    result = connection.execute(text("""
        SELECT * FROM Students
        WHERE age > 22
    """))

    print("\nStudents older than 22:")

    for row in result:
        print(row)

# Select only name and Course column from the Students table

with engine.connect() as connection:
    result = connection.execute(text("""
        SELECT name, course FROM Students
        """))
    print("\nStudents name and course:")

    for row in result:
        print(row)

# Update student data in the Students table

with engine.connect() as connection:
    connection.execute(text("""
        UPDATE Students
        SET age = 24
        WHERE id = 101
    """))

    connection.commit()

print("\nStudent data updated successfully!")

# Check the updated data
with engine.connect() as connection:
    result = connection.execute(text("""
        SELECT * FROM Students
        WHERE id = 101
    """))

    print("\nUpdated Student Record:")

    for row in result:
        print(row)

# Delete student data from the Students table

with engine.connect() as connection:
    connection.execute(text("""
        delete from Students
        where id = 105
    """))
    connection.commit()

print("\nStudent data deleted successfully!")

# Check the remaining data
with engine.connect() as connection:
    result = connection.execute(text("""
        select * from Students
    """))
    print("\nRemaining student records:")
    for row in result:
        print(row)