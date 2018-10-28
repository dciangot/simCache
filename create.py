from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'simCache'

TABLES = {}
TABLES['sites'] = (
    "CREATE TABLE `sites` ("
    "  `name` varchar(48) NOT NULL,"
    "  `country` varchar(48) NOT NULL,"
    "  `tier` varchar(48) NOT NULL,"
    "  `tfc` varchar(48) NOT NULL,"
    "  PRIMARY KEY (`name`)"
    ") ENGINE=InnoDB")

TABLES['jobs'] = (
    "CREATE TABLE `jobs` ("
    "  `id` varchar(48) NOT NULL,"
    "  `dataset` varchar(256) NOT NULL,"
    "  `site` varchar(48) NOT NULL,"
    "  `destination` varchar(48) NOT NULL,"
    "  `cpuEff` varchar(48) NOT NULL,"
    "  `cpuTime` varchar(48) NOT NULL,"
    "  PRIMARY KEY (`dataset`)"
    ") ENGINE=InnoDB")

try:
    cnx = mysql.connector.connect(user='root', password='passwd',
                                  host='127.0.0.1')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = cnx.cursor()


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
