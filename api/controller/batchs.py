from server import app
from flask import jsonify
from api.model.batch import Batch

@app.route('/batchs')
def get_batch():
    r = Batch.query.all()
    return jsonify({"data": r})
