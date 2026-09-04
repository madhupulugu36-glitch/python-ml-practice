from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/students/<int:id>")
def student_by_id(id):

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

    for student in students:
            if student["id"] == id:
                 return jsonify(student)
    return jsonify({"message": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)