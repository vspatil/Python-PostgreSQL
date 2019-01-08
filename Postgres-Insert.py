import psycopg2

conn = psycopg2.connect(database="test", user="postgres", password="r00t1!", host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute ("insert into emp (empid,Empname,deptid,salary)\
             values ('3','John','200','6000')");

cur.execute ("insert into emp (empid,Empname,deptid,salary)\
             values ('4','Adam','200','8000')");

conn.commit()
conn.close()
