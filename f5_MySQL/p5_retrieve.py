import pymysql
meradb=pymysql.connect(host="localhost",user="root",password="Vishwajit@2001",database="db")
cur=meradb.cursor()
cur.execute("select * from book;")
result=cur.fetchall()
for rec in result:
    print(rec)
