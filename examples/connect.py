#!/usr/bin/python
import cx_Oracle
 


# Connect string format: [username]/[password]@//[hostname]:[port]/[DB service name]
conn = cx_Oracle.connect("system/GetStarted18c@//localhost:1521/XEPDB1")
cur = conn.cursor()
cur.execute("SELECT 'Hello World!' FROM dual")
res = cur.fetchall()
print(res)
