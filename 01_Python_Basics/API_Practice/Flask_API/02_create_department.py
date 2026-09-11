from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.engine import URL
connection_url = URL.create(
    drivername="mysql+mysqlconnector",
    username="root",
    password="Madhu@8466",
    host="localhost",
    port=3306,
    database="sqlalchemy_01"  
 )
engine = create_engine(connection_url)

print("Database engine created Successfully")

metadata = MetaData()

departments = Table(
    "departments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("location", String(100))
)

metadata.create_all(engine)

print()