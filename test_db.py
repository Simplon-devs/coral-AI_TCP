import mysql.connector
import pytest

@pytest.fixture
def connection(database='Reefscapers2020_v2'):
    conn = mysql.connector.connect(
        host="localhost",
        database=database,
        user="root",
        password="root",
    )
    yield conn
    conn.close()