import sqlite3
from practica2 import InterfaceManager
from extras.utils import (get_conn)

def test_get_conn():
    conn = get_conn()
    assert isinstance(conn, sqlite3.Connection)

def test_render_user():
    interface_manager = InterfaceManager()
    users = interface_manager.render_user()
    assert type(users) == type(list())

def test_redirect(mocker):
    mocker.patch.object(InterfaceManager(), 'home', return_value=True)

    interface_manager = InterfaceManager()
    assert interface_manager.redirect(5) == True