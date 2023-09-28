import pymysql
meradb=pymysql.connect(host="localhost",user="root",password="Vishwajit@2001",database="db")
cur=meradb.cursor()
cur.execute("DELETE FROM book WHERE title='Python'")
meradb.commit()