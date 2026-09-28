from flask import Flask, jsonify, request
from db import engine
from models import Student


app = Flask(__name__)


@app.route("/")
def home():
    return {
        "message": "Student Management API is running"
    }
    
@app.route("/students", methods=["GET"])
def get_students():
    with engine.connect() as connection:
        result = connection.execute(
            Student.__table__.select()
        )
        
        students = []
        for row in result:
            students.append({
                "id": row.id,
                "name": row.name,
                "age": row.age,
                "course": row.course
            })
        return jsonify(students)

@app.route("/students", methods=["POST"])
def add_student():
    
    data = request.get_json()
    
    name = data["name"]
    age = data["age"]
    course = data["course"]
    
    with engine.begin() as connection:
        result = connection.execute(
            Student.__table__.insert().values(
                name = name,
                age = age,
                course = course
            )
        )
    
    return{"message": "Student added successfully"},201

@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):

    with engine.connect() as connection:

        result = connection.execute(
            Student.__table__.select().where(Student.id == id)
        )

        row = result.fetchone()

        if not row:
            return {"message": "Student not found"}, 404

        return {
            "id": row.id,
            "name": row.name,
            "age": row.age,
            "course": row.course
        }, 200
        
@app.route("/students/<int:id>", methods=["PUT"])
def update_students(id):
    
    data = request.get_json()
    
    with engine.begin() as connection:
        
        result = connection.execute(
            Student.__table__.select().where(Student.id ==id)
        )
        
        student = result.fetchone()
        
        if not student:
            return {"message": "student not founded"}, 404
        connection.execute(
            Student.__table__.update().where(Student.id == id)
            .values(
                name=data["name"],
                age=data["age"],
                course=data["course"]
            )
            
        )
    return {"message": "Student Updated Successfully"}, 200

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    
    with engine.begin() as connection:
        result = connection.execute(
            Student.__table__.select().where(Student.id == id)
        )
        
        student = result.fetchone()
        
        if not student:
            return {"message": "Student not Found"}, 404
        connection.execute(
            Student.__table__.delete().where(Student.id == id)
        )
        
    return {"message": "Student Deleted Successfully"}, 404
    

if __name__ == "__main__":
    app.run(debug=True)