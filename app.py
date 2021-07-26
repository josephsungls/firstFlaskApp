from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/hello")
def hello():
    return "Hi There "

@app.route("/hello/<string:name>/")
def getName(name):
    return name</string:name>

if __name__ == "__main__":
    app.run()