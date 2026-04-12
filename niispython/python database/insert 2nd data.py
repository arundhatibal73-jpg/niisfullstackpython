import sqlite3
conn=sqlite3.connect("student.db")
cur=conn.cursor()
cur.execute("INSERT INTO student VALUES(2,'gita',88)")
conn.commit()
conn.close()
print("data inserted successfully")      	