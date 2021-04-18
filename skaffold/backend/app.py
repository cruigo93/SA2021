import os
import json
import random
import uuid
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/health", methods=["GET"])
def health():
    return {"status": "OK"}, 200


@app.route("/")
def hello():
    return {"response": "Testing " + os.environ['HOSTNAME'] + "!"}, 200


@app.route("/get")
def get():

    users = []
    for _ in range(10):
        user_id = str(uuid.uuid4())
        name = "User"+str(random.randint(0, 100))
        user = {
            "user_id": user_id,
            "name": name
        }
        users.append(user)
    return {"users": [users]}, 200


@app.route("/version")
def version():
    return {"version": "1.0.0"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


