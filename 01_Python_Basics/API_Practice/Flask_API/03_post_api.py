from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Madhu",
        "course": "Python ML"
    },
    {
        "id": 2,
        "name": "Rahul",
        "course": "Data Science"
    },
    {
        "id": 3,
        "name": "Priya",
        "course": "Python"
    }
]


# GET - Get all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


# POST - Create a new student
@app.route("/students", methods=["POST"])
def create_student():

    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body is required"}), 400

    if "name" not in data:
        return jsonify({"message": "Name is required"}), 400

    if "course" not in data:
        return jsonify({"message": "Course is required"}), 400

    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "course": data["course"]
    }

    students.append(new_student)

    return jsonify(new_student), 201


# PUT - Update an existing student
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body is required"}), 400

    for student in students:

        if student["id"] == id:

            if "name" in data:
                student["name"] = data["name"]

            if "course" in data:
                student["course"] = data["course"]

            return jsonify(student), 200

    return jsonify({"message": "Student not found"}), 404


# DELETE - Delete an existing student
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    for student in students:

        if student["id"] == id:

            students.remove(student)

            return jsonify({
                "message": "Student deleted successfully",
                "student": student
            }), 200

    return jsonify({
        "message": "Student not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)