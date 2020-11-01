# Quên tạo cột cần thêm trường cho databaseimport mysql.connector
import mysql.connector
 
# tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "anthanh",
        passwd = "25041999", database = "PythonDB")
   
# tạo đối tượng cursor
cur = myconn.cursor()  
   
try:
    # thêm cột branch name vào bảng Employee
    cur.execute("alter table Employee add branch_name varchar(20) not null")
except:
    myconn.rollback()
 
myconn.close()