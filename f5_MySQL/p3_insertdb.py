import pymysql
meradb=pymysql.connect(host="localhost",user="root",password="Vishwajit@2001",database="db")
cur=meradb.cursor()
s="insert into book(bookid,title,price)values(%s,%s,%s)"
b=(1,"Python",34.2)
cur.execute(s,b)

#We need to ensure that we do commit or else it won't be save into the db
meradb.commit()