from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    #now=datetime.now()
    #current_time=now.strftime("%H:%M:%S")
    #return "Hi there, the time is " + current_time
    return "Hello World"

if __name__ == "__main__":
    app.run(host="172.31.31.208", port=80)