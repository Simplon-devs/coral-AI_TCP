import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb as MS
import mysql
import mysql.connector


def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    # YOUR CODE
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="db_coral_planters",
        auth_plugin='caching_sha2_password'
        )

def Create_db(db_name):
    db = MS.connect(host="localhost",user="root",passwd="root")
    
    #Drop database
    cursor = db.cursor()
    db_name = 'reeftest'
    cursor.execute(f'DROP DATABASE IF EXISTS {db_name}')
    
    # Create database
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')
    
    db.commit()
    
    return db


def Create_table(db_name):
    db = MS.connect(host="localhost", user="root", passwd="root", database=db_name)
    cursor = db.cursor()
    # Create table 
    cursor.execute('''CREATE TABLE foo (
       bar VARCHAR(50) DEFAULT NULL
       )''')
    
    #Insert data    
    cursor.execute('INSERT into foo (bar) values (4)')
    
    # Commit your changes in the database
    db.commit()
    
    return db