import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

from models import Base


# Load variables from .env
load_dotenv()


DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("MYSQL_USERNAME"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
    database=os.getenv("MYSQL_DATABASE")
)


engine = create_engine(DATABASE_URL)


try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

        print("MySQL connection successful")
        print("Result:", result.scalar())

    Base.metadata.create_all(engine)

    print("Employees table checked successfully")

except Exception as e:
    print("Database connection failed")
    print("Error:", e)