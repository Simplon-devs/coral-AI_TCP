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

def test_select(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM annotations WHERE AnnotationId = 404")
    result = cursor.fetchone()
    assert result[0] == 1