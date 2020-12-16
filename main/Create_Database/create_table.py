import mysql.connector
 
# tạo đối tượng connection
mydb = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    passwd = "admin999999999", 
    database = "uet")
   
# tạo đối tượng cursor
mycursor = mydb.cursor()
   
try:
    # tạo bảng Employee gồm 4 cột name, id, salary, và department id  
    dbs = mycursor.execute("create table sensors(Area varchar(20) not null, "
        + "ID int not null, "
        + "Temperature float not null, "
        + "Humidity float not null)")
except:
    mycursor.rollback()
 
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
mycursor.close()