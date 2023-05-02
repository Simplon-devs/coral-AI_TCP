import pytest
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb as MS

from bdd import Create_db, Create_table, OpenMydb

def test_create_db():
    
    # A enlever lorsque la base de donnée sera publié
    db = Create_db('Test_Reefscapers2020_v2')
    
    op = OpenMydb('Test_Reefscapers2020_v2')
    assert op is not None
    db.close()

    
def test_create_table():
    db_name = 'Test_Reefscapers2020_v2'
    Create_db (db_name)
    db = Create_table(db_name)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM foo')
    result = cursor.fetchone()
    assert result[0] == '4'
    db.close()

    