import sqlite3

conn=sqlite3.connect('legumes.db')
c=conn.cursor()
c.execute("SELECT * FROM LEGUMES")
base=c.fetchall()
print(base)