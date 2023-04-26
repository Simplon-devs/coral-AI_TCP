import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb as MS

def Create_db(db_name):
    db = MS.connect(host="localhost",user="root",passwd="root")
    
    #Drop database
    cursor = db.cursor()
    cursor.execute(f'DROP DATABASE IF EXISTS {db_name}')
    
    # Create database
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')
    
    db.commit()
    
    return db

def OpenMydb(db_name):

    # Opens the specified database

    db = MS.connect(host="localhost", user="root", passwd="root", db=db_name)
    db.autocommit(True)
    
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