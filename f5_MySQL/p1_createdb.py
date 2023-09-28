# Import the mysql.connector module, which allows you to connect to MySQL databases using Python.
import pymysql
#mysql.connector


# .connect is the database connection object
meradb = pymysql.connect(host="localhost", user="root", password="Vishwajit@2001")


# cursor is the method of the connection object
cur = meradb.cursor()

# Execute an SQL command to create a new database.
cur.execute("create database db")

