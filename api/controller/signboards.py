from server import app
from flask import jsonify
from api.model.signboard import Signboard

@app.route('/signboards')
def get_signboard():
    r = Signboard.query.all()
    return jsonify({"data": r})
