import MySQLdb

def OpenMydb(database="Reefscapers2020_v2"):

    # Opens the specified database

    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db=database)
    db.autocommit(True)
    return db