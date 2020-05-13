import os
import tempfile
import pytest
import server
import json
from base_test_machine import *


def test_get_signboards(client):
    """ GET signboards """
    rv = client.get('/signboards')
    assert rv.status == "200 OK"
