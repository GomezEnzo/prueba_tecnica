import pytest

from practica1 import (RequestWs, DataManager)
from websocket import create_connection

def test_connect_ws():
    rq = RequestWs()
    ws = rq.connect_ws()
    assert hasattr(ws, "status")

def test_request(mocker):
    mocker.patch.object(RequestWs, "connect_ws", return_value=create_connection("ws://209.126.82.146:8080"))
    rq = RequestWs()
    elements = rq.request()

    assert len(elements) == 60000


def test_data_validation():
    elements = [
    {'a': 98, 'b': 159357},
    {'a': 57, 'b': 17760}
    ]

    expected_dict = {
            'max_num': 159357,
            'min_num': 17760,
            'even_numbers': 1,
            'odd_numbers': 1,
            'prime_numbers': 0,
            'first_number': 159357,
            'last_number': 17760
        }
    dm = DataManager()
    data = dm.data_validation(elements)

    assert data == expected_dict

