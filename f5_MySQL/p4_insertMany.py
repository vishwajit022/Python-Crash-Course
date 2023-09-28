import pymysql
meradb=pymysql.connect(host="localhost",user="root",password="Vishwajit@2001",database="db")
cur=meradb.cursor()

s="insert into book(bookid,title,price)values(%s,%s,%s)"
list_of_tuples=[(4,"Java",45.2),(5,"C",45.3),(6,"C++",34.3)]

cur.executemany(s,list_of_tuples)

meradb.commit()

#Another way to write the program

import pymysql

def data_generator():
    yield (4, "Java", 45.2)
    yield (5, "C", 45.3)
    yield (6, "C++", 34.3)

meradb = pymysql.connect(host="localhost", user="root", password="Vishwajit@2001", database="db")
cur = meradb.cursor()

s = "INSERT INTO book (bookid, title, price) VALUES (%s, %s, %s)"

cur.executemany(s, data_generator())
meradb.commit()
