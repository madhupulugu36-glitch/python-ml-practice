from sqlalchemy import create_engine, text

# Create database engine
engine = create_engine("sqlite:///students.db")

print("Database engine created successfully")

# One connection for all operations
with engine.connect() as connection:

    # CREATE TABLE
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            course TEXT
        )
    """))

    print("Student table created successfully")

    # INSERT
    connection.execute(text("""
        INSERT INTO students (name, age, course)
        VALUES ('Madhu', 29, 'Python')
    """))

    connection.commit()

    print("Student inserted successfully")

    # SELECT
    result = connection.execute(text("""
        SELECT name, age, course
        FROM students
    """))

    print("\nStudent Details:")

    for row in result:
        print("Name:", row.name)
        print("Age:", row.age)
        print("Course:", row.course)
        print("---")

     # SELECT with WHERE
    result = connection.execute(text("""
        SELECT name, age, course
        FROM students
        WHERE age = 29
    """))

    print("\nStudents with age 29:")

    for row in result:
     print("Name:", row.name)
     print("Age:", row.age)
     print("Course:", row.course)   

    # UPDATE student
    connection.execute(text("""
        UPDATE students
        SET course = 'SQLAlchemy'
        WHERE name = 'Madhu'
    """))

    connection.commit()

    print("\nStudent course updated successfully") 

    # Verify UPDATE
    result = connection.execute(text("""
        SELECT name, age, course
        FROM students
        WHERE name = 'Madhu'
    """))

    for row in result:
        print("Name:", row.name)
        print("Age:", row.age)
        print("Course:", row.course)

    # Show student IDs
    result = connection.execute(text("""
        SELECT id, name, age, course
        FROM students
    """))

    print("\nCurrent students:")

    for row in result:
        print(row)
    # DELETE
    connection.execute(text("""
        DELETE FROM students
        WHERE age = 29
    """))

    connection.commit()

    print("Student deleted successfully")

    # Verify DELETE
    result = connection.execute(text("""
        SELECT id, name, age, course
        FROM students
    """))

    print("\nStudents after DELETE:")

    for row in result:
        print(row)