from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/student")
def student():
    data = {
        "id": 1,
        "name": "Madhu",
        "course": "Python ML"
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)