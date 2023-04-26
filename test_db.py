import pytest
import pymysql
pymysql.install_as_MySQLdb()

from bdd import Create_db, Create_table

def test_create_db():
    db = Create_db('reeftest')
    assert db is not None
    db.close()

    
def test_create_table():
    db_name = 'reeftest'
    Create_db (db_name)
    db = Create_table(db_name)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM foo')
    result = cursor.fetchone()
    assert result[0] == '4'
    db.close()

    