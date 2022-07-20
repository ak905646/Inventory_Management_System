import sqlite3
con = sqlite3.connect('ims.db')
cur = con.cursor()
cur.execute('select * from employee')
rows =  cur.fetchall()
print(type(rows[0]))