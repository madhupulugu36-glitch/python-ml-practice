from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello madhu! My First Flask API"

@app.route("/about")
def about():
    return "This is my Flask API"

if __name__ =="__main__":
    app.run(debug=True)