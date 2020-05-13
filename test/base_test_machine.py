import os
import tempfile
import pytest
import server
import json

from server import db
from api.model.batch import Batch
from api.model.signboard import Signboard

def make_batch():
    b = Batch().query.filter_by(batch_code="batch1").first()
    if not b:
        batch = Batch()
        batch.batch_code = "batch1"
        db.session.add(batch)
        db.session.commit()

def make_signboard():
    b = Signboard().query.filter_by(signboard_code="signboard1").first()
    if not b:
        signboard = Signboard()
        signboard.signboard_code = "signboard1"
        db.session.add(signboard)
        db.session.commit()


@pytest.fixture
def client():
    db_fd, server.app.config['DATABASE'] = tempfile.mkstemp()
    server.app.config['TESTING'] = True

    with server.app.test_client() as client:
        with server.app.app_context():
            # server.init_db()
            pass
        yield client

    os.close(db_fd)
    os.unlink(server.app.config['DATABASE'])


