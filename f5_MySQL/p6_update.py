import pymysql
meradb=pymysql.connect(host="localhost",user="root",password="Vishwajit@2001",database="db")
cur=meradb.cursor()

cur.execute("UPDATE book SET price=price+200 WHERE price>40")
meradb.commit()