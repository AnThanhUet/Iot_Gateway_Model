import mysql.connector
   
# tạo đối tượng connection
myconn = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    passwd = "admin999999999")
 
# tạo đối tượng cursor
cur = myconn.cursor()
 
try:
    cur.execute("create database PythonDB")
    dbs = cur.execute("show databases")
except:
    myconn.rollback()
for x in cur:
    print(x)
myconn.close()