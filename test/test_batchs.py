import os
import tempfile
import pytest
import server
import json
from base_test_machine import *


def test_get_batchs(client):
    """ GET batchs """
    rv = client.get('/batchs')
    assert rv.status == "200 OK"
