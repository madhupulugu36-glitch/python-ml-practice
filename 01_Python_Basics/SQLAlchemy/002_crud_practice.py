from sqlalchemy import create_engine, text

# 1. Creating Database Engine
engine = create_engine("sqlite:///crud_practice.db")
print("crud database created successfully")

# 2. Connect to database
with engine.connect() as connection:
    #====================
    # 3. Create
    #====================
    connection.execute(text("""
        create table if not exists employees(
            id integer primary key,
            name text,
            age integer,
            role text,
            salary integer
        )
    """))
    connection.commit()
    print("Employees Table created successfully")

    #====================
    # 4. INSERT
    #====================
    connection.execute(text("""
        delete from employees
    """))
    connection.commit()

    connection.execute(text("""
        insert into employees(name, age, role, salary)
        values
        ('Rahul', 28, 'Python Developer', 50000),
        ('Priya', 30, 'QA Engineer', 45000),
        ('Arjun', 26, 'Data Analyst', 55000)
    """))
    connection.commit()

    print("Employees inserted Successfully")

    #=====================
    # 5. SELECT
    #=====================
    result = connection.execute(text("""
        select * from employees
    """))
    print("\nAll Employees:")
    for row in result:
        print(row)

    #====================
    #Where
    #====================
    result = connection.execute(text("""
        select name, role, salary from employees
        where salary > 50000
    """))
    print("\nEmployees salary greaterthen 50000" \
    "")
    for row in result:
        print("Name:", row.name)
        print("Role:", row.role)
        print("Salary:", row.salary)
        print("================")

    #=================
    #UPDATE
    #=================
    connection.execute(text("""
        update employees
        SET salary = 50000
        where id = 2
    """))
    connection.commit()
    print("\nPriya's salary updated successfully")

    #=================
    #VERIFY DATA
    #=================
    result = connection.execute(text("""
        select id, name, role, salary from employees
        where id = 2
    """))
    for row in result:
        print("Name:", row.name)
        print("Role:", row.role)
        print("Salary:", row.salary)