import mysql.connector

DB = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '3699',
)

cursorObject = DB.cursor()

cursorObject.execute("CREATE DATABASE fabrics")

print("ALL DONE!")