import os
import tempfile
import pytest
import server
import json

from base_test_machine import client


def test_index(client):
    """ test homepage."""
    rv = client.get('/')
    assert rv.status == "200 OK"
    json_resp = json.loads(rv.data)
    assert json_resp["message"] == "hello world"

