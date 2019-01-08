import psycopg2

conn = psycopg2.connect(database='test',user='postgres',password='r00t1!',host='localhost',port=5432)
print("Database connected")

cur = conn.cursor()
cur.execute("Delete from emp where empid = 5")
conn.commit()

cur.execute("select * from emp order by empid")
rows = cur.fetchall()
for row in rows:
    print(row[0],str(row[1]),row[2],row[3])

conn.close()