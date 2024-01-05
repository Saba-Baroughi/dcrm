import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='saba',

)
#preapare a cursor object
cursorobject=database.cursor()

#create a database
cursorobject.execute("CREATE DATABASE elderco")
print("All Done!")