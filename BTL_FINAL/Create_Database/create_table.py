import mysql.connector
 
# tạo đối tượng connection
mydb = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    passwd = "admin999999999", 
    database = "PythonDB")
   
# tạo đối tượng cursor
mycursor = mydb.cursor()
   
try:
    # tạo bảng Employee gồm 4 cột name, id, salary, và department id  
    dbs = mycursor.execute("create table world(name varchar(20) not null, "
        + "id int(20) not null primary key, "
        + "u float not null, "
        + "i int not null, "
        + "w int not null)")
except:
    mycursor.rollback()
 
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
mycursor.close()