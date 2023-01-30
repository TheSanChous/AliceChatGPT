from src import handler
from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    return handler(request.get_json())


if __name__ == "__main__":
    app.run(debug=True)
