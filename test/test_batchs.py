import os
import tempfile
import pytest
import server
import json
from base_test_machine import *
from api.model.batch import Batch


def test_get_batchs(client):
    """ GET batchs """
    make_batch()
    rv = client.get('/batchs')
    assert rv.status == "200 OK"
    data = json.loads(rv.data)["data"]
    assert data[0]["batch_code"] == "batch1"

def test_delete_batch(client):
    """ DELETE batch """
    rv = client.delete('/batchs/batch1')
    assert rv.status == "200 OK"
    json_resp = json.loads(rv.data)
    assert json_resp["Message"] == "Delete done"

