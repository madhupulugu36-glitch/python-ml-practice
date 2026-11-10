
import os
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# Read database credentials from environment variables
DB_USER = os.getenv("AI_HEALTH_DB_USER", "root")
DB_PASSWORD = os.getenv("AI_HEALTH_DB_PASSWORD")
DB_HOST = os.getenv("AI_HEALTH_DB_HOST", "localhost")
DB_PORT = int(os.getenv("AI_HEALTH_DB_PORT", "3306"))
DB_NAME = "ai_health_monitoring"

if not DB_PASSWORD:
    raise RuntimeError(
        "Set the AI_HEALTH_DB_PASSWORD environment variable first."
    )

database_url = URL.create(
    drivername="mysql+mysqlconnector",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)

engine = create_engine(
    database_url,
    pool_pre_ping=True,
)

def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT VERSION()"))
        print("Connected to MySQL successfully!")
        print("MySQL version:", result.scalar())


if __name__ == "__main__":
    test_connection()