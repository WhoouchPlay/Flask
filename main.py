from flask import Flask

app = Flask(__name__)

@app.route("/todolist")
def todolist():
    return ["1. Wake Up", "2. Play game", "3. Homework"]

@app.route("/")
def hello():
    return "Hello!"

app.run(port=16261, debug=True)