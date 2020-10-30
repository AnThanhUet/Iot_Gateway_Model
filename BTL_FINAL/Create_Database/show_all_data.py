# Phuong thuc fetchall() tra ve data luu trong bang duoi dang cac hang
import mysql.connector
 
#tạo đối tượng connection
myconn = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    passwd = "admin999999999", 
    database = "PythonDB")
 
#tạo đối tượng cursor
cur = myconn.cursor()
 
try:
    # select dữ liệu từ database
    cur.execute("SELECT * FROM Employee")
     
    # tìm nạp các hàng từ đối tượng con trỏ  
    result = cur.fetchall()
 
    for x in result:
        print(x)
 
except:
    myconn.rollback()
 
myconn.close()