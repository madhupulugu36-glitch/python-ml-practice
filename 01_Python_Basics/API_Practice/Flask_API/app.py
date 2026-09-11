from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Welcome to Flask basics by youtube </h1>"

@app.route("/courses")
def courses():
    return "Welcome to the courses"
if __name__ == "__main__":
    app.run(debug=True)