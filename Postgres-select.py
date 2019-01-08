import psycopg2
conn = psycopg2.connect(database="test", user="postgres", password="r00t1!", host="127.0.0.1", port="5432")
print("Database Connected")
cur = conn.cursor()
cur.execute("select * from emp")

rows = cur.fetchall()

for row in rows:
    print(row[0],str(row[1]),row[2],row[4])
conn.close()
