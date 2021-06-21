from flask import Flask, request
from src.controller.SplitStringController import splitString

app = Flask(__name__)

@app.route("/test", methods=["POST"])
def test():
    return splitString(request)

if __name__ == "__main__":
	app.run()
