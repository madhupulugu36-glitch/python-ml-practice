from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from models import Base


DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Madhu8466",
    host="localhost",
    port=3306,
    database="sqlalchemy_01"
)


engine = create_engine(DATABASE_URL)


try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

        print("MySQL connection successful")
        print("Result:", result.scalar())

except Exception as e:
    print("Database connection failed")
    print("Error:", e)


Base.metadata.create_all(engine)

print("Employees table checked successfully")