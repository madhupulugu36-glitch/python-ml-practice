from flask import Flask, jsonify
from sqlalchemy import select
from sqlalchemy.orm import Session

from db import engine
from models import Employee


app = Flask(__name__)


@app.route("/")
def home():
    return "Flask + MySQL API"


@app.route("/employees", methods=["GET"])
def get_employees():

    with Session(engine) as session:

        statement = select(Employee)

        employees = session.scalars(statement).all()

        employee_list = []

        for employee in employees:
            employee_list.append({
                "id": employee.id,
                "name": employee.name,
                "age": employee.age,
                "job": employee.job,
                "salary": employee.salary
            })

        return jsonify(employee_list)


if __name__ == "__main__":
    app.run(debug=True)