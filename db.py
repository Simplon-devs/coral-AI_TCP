import sqlite3
from sqlite3 import Error
import click
from flask import current_app, g, jsonify

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    # YOUR CODE
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()



def init_db():
    db = get_db()

    with current_app.open_resource('db_coral_planters.sql') as f:
        db.executescript(f.read().decode('utf8'))

def selectAnnotations(conn):
    cur = conn.cursor()
    id = 405
    cur.execute(f'''
    SELECT * FROM annotations
    WHERE AnnotationId = {id}
    
                 ''')
    rows = cur.fetchall()

    objects_list = []
    for row in rows:
        d = []
        d['Type'] = row[0]
        d['Score'] = row[1]
        objects_list.append(d)
        print(d, objects_list)
    return jsonify(objects_list[0])


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')