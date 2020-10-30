import mysql.connector
 
#tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "anthanh",
    passwd = "25041999", database = "PythonDB")
 
#tạo đối tượng cursor
cur = myconn.cursor()
 
try:
    # cập nhật name cho bảng Employee
    cur.execute("delete from Employee where id = 10001")
    myconn.commit()
 
except:
    myconn.rollback()
 
myconn.close()