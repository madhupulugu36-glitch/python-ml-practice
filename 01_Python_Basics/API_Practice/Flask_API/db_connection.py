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

metadata = MetaData()

employees = Table(
    "employees",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("age", Integer),
    Column("job", String(100)),
    Column("salary", Integer)
)

metadata.create_all(engine)

print("Employees table created successfully!")

#with engine.begin() as connection:
#    connection.execute(
#        employees.insert(),
 #       [
  #          {
   #             "name": "Rahul",
    #            "age": 28,
     #           "job": "Python Developer",
      #          "salary": 50000
       #     },
        #    {
         #       "name": "Priya",
          #      "age": 30,
           #     "job": "QA Engineer",
            #    "salary": 45000
            #},
            #{
             #   "name": "Arjun",
              #  "age": 26,
               # "job": "Data Analyst",
                #"salary": 55000
          #  }
       # ]
   # )

#print("Employees inserted successfully!")

with engine.connect() as connection:
    result = connection.execute(employees.select())

    print("\nAll Employees:")

    for row in result:
        print(row)
