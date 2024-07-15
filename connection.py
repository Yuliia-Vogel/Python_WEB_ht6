import sqlite3
from contextlib import contextmanager


database = './university.db'


@contextmanager
def create_connection(database):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(database)
    yield conn
    conn.rollback()
    conn.close()