import os

from flask import Flask, request
from werkzeug.exceptions import BadRequest

from functions import build_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST"])
def perform_query():
    try:
        query = request.args["query"]
        file_name = request.args["file_name"]
    except KeyError:
        raise BadRequest

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return BadRequest(description=f"{file_name} not found")

    with open (file_path, "r") as f:
        res = build_query(f, query)
        content = '\n'.join(res)
    return app.response_class(content, content_type="text/plain")


if __name__ == "__main__":
    app.run()
