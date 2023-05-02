import mysql
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

    db = MS.connect(host="localhost", user="root", passwd="", db=db_name)
    cursor = db.cursor()
    db.autocommit(True)
    
    return db, cursor



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


def insert_buyers():

    #insert buyers id, take from table utilisateurs every id wich have 'user' role
    # ne pas oublier de les insérer au bon endroit dans le code (!)
    request = """INSERT INTO buyers (id_buyers)
SELECT id FROM utilisateurs WHERE `role`='user';"""

def attribute_Acropora():

    #attribute afragmentID to a user wich has been transplanted since less than 8 months. The user by an acropora
    #doit attribuer un fragment du bon type qui n'est pas mort, tombé ou blanchis
    # ne pas oublier de les insérer au bon endroit dans le code (!)
    request = """UPDATE `buyers`
    SET `fragment_id` = IFNULL(`fragment_id`, (
	SELECT `FragmentId` FROM `fragments`
    WHERE `Transplanted` > DATE_SUB(NOW(), INTERVAL 8 MONTH) AND `type` = 'Acropora'
    ORDER BY RAND() LIMIT 1
    ))
    WHERE `fragment_id` IS NULL;"""

# def attribute_Pocilopora():

#     #attribute afragmentID to a user wich has been transplanted since less than 8 months. The user by an acropora
#     #doit attribuer un fragment du bon type qui n'est pas mort, tombé ou blanchis
#     # ne pas oublier de les insérer au bon endroit dans le code (!)
#     request = """UPDATE `buyers`
#     SET `fragment_id` = IFNULL(`fragment_id`, (
# 	SELECT `FragmentId` FROM `fragments`
#     WHERE `Transplanted` > DATE_SUB(NOW(), INTERVAL 8 MONTH) AND `type` = 'Pocilopora'
#     ORDER BY RAND() LIMIT 1
#     ))
#     WHERE `fragment_id` IS NULL;"""

# def user_coral_infos():
#     #get informations for client, it'll be a sentence with informations
#     #ne pas oublier de les insérer au bon endroit dans le code (!) 

# def bbox_coral_reconstit():
#     #display picture with bonding box of coral 
#     #ne pas oublier de les insérer au bon endroit dans le code (!)
