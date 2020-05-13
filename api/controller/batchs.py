import json

from api.utils.alchemy_encoder import AlchemyEncoder
from server import app, db
from flask import jsonify
from api.model.batch import Batch

@app.route('/batchs')
def get_batch():
    r = Batch.query.all()
    return jsonify({"data": json.loads(json.dumps(r, cls=AlchemyEncoder))})

@app.route('/batchs/<string:batch_code>', methods=['DELETE'])
def delete_batch(batch_code):
    b = Batch.query.get(batch_code)
    if (b is None):
        return jsonify({"error": 'batch_code does not exists'})
    b.deleted = True
    db.session.commit()
    return jsonify({"status": 200, "Message": 'Delete done'})
