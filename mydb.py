# install mysql
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

config = {
    "user": "root",
    "password": "admin",
    "host": "localhost",
    # "port": "3306",
    # "raise_on_warnings": True,
}


dataBase = mysql.connector.connect(**config)

# Prepare a cursor obj
cursorObj = dataBase.cursor()

# Create a database
cursorObj.execute("CREATE DATABASE customerTable")

print("all done")
