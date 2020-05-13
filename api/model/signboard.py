from server import db
from datetime import datetime

class Signboard(db.Model):

    signboard_code = db.Column(db.String, primary_key=True)
    author = db.Column(db.String(120))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    signboard_status = db.Column(db.String(120))
    url = db.Column(db.String(120))
    deleted = db.Column(db.Boolean)

    def __repr__(self):
        return '<Signboard %r>' % self.signboard_code