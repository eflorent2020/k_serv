import os
import tempfile
import pytest
import server
import json
from base_test_machine import *
from api.model.signboard import Signboard


def test_get_signboards(client):
    """ GET signboards """
    make_signboard()
    rv = client.get('/signboards')
    assert rv.status == "200 OK"
    data = json.loads(rv.data)["data"]
    assert data[0]["signboard_code"] == "signboard1"

def test_delete_signboard(client):
    """ DELETE signboard """
    rv = client.delete('/signboards/signboard1')
    assert rv.status == "200 OK"
    json_resp = json.loads(rv.data)
    assert json_resp["Message"] == "Delete done"