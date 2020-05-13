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