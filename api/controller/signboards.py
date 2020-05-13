import json

from api.utils.alchemy_encoder import AlchemyEncoder
from server import app, db
from flask import jsonify
from api.model.signboard import Signboard

@app.route('/signboards')
def get_signboard():
    r = Signboard.query.all()
    return jsonify({"data": json.loads(json.dumps(r, cls=AlchemyEncoder))})

@app.route('/signboards/<string:signboard_code>', methods=['DELETE'])
def delete_signboard(signboard_code):
    b = Signboard.query.get(signboard_code)
    if (b is None):
        return jsonify({"error": 'signboard_code does not exists'})
    b.deleted = True
    db.session.commit()
    return jsonify({"status": 200, "Message": 'Delete done'})