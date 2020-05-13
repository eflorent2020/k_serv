import json

from api.utils.alchemy_encoder import AlchemyEncoder
from server import app
from flask import jsonify
from api.model.batch import Batch

@app.route('/batchs')
def get_batch():
    r = Batch.query.all()
    return jsonify({"data": json.loads(json.dumps(r, cls=AlchemyEncoder))})
