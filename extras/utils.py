import sqlite3

# Return sqlite3 connector
def get_conn():
    return sqlite3.connect('prueba.db')

# class decorator for singleton pattern
def singleton(cls):
    instances = {}

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]
    return wrap