from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    now=datetime.now()
    current_time=now.strftime("%H:%M")
    return "Hi there, the time is " + current_time

if __name__ == "__main__":
    app.run()