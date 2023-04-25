import pytest
import MySQLdb
from bdd import OpenMydb

def test_OpenMydb():
    db = OpenMydb(database="Reefscapers2020_v2")
    assert isinstance(db, MySQLdb.connections.Connection)

def test_select():
    db = OpenMydb()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM annotations WHERE AnnotationId = 404")
    result = cursor.fetchone()
    assert result[0] == 1
    db.close()