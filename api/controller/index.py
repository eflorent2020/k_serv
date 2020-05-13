from server import app
from flask import jsonify

@app.route('/')
def hello_world():
    return jsonify({"message": "hello world"})

@app.route('/signboard/:customer_code/:signboard_code')
def signboard():
    return jsonify({"message": "good"})
