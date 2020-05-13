import os
import tempfile
import pytest
import server
import json


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


