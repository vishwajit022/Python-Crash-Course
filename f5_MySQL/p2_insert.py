import pymysql

# Connect to the 'db' database when establishing the connection.
meradb = pymysql.connect(host="localhost", user="root", password="Vishwajit@2001", database="db")

# Create a cursor object.
cur = meradb.cursor()

s="CREATE TABLE book (bookid INT(4), title VARCHAR(20), price DECIMAL(5, 2))"
# Now you can execute your SQL queries on the 'db' database.
cur.execute(s)

