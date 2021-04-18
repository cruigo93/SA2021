import os
import json
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/health", methods=["GET"])
def health():
    return {"status": "OK"}, 200


@app.route("/")
def hello():
    return {"response": "Testing " + os.environ['HOSTNAME'] + "!"}


