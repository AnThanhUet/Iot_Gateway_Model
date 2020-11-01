import mysql.connector
 
#tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "anthanh",
    passwd = "25041999", database = "PythonDB")
 
#tạo đối tượng cursor
cur = myconn.cursor()
sql = ("insert into Employee(name, id, salary, dept_id, branch_name) "
    "values (%s, %s, %s, %s, %s)")
 
#giá trị của một row được cung cấp dưới dạng tuple
val = [("Vinh", 10002, 26000.00, 101, "Hanoi"), 
       ("Trung", 10003, 26000.00, 102, "Danang")]
 
try:
    #inserting the values into the table
    cur.executemany(sql, val)
 
    #commit the transaction
    myconn.commit()
 
except:
    myconn.rollback()
 
print(cur.rowcount,"record inserted!")
myconn.close()