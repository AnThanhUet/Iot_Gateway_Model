# raspbery_gateway

## How to install

1.Install pip
```
    sudo apt install python3-pip
```
2.Check pip 
```
    pip3 --version
```
3.Install lib Paho MQTT Python Client  
```
    pip3 install paho-mqtt
    // Import paho.mqtt.client as mqtt
```
## Connecting to MySQL using Python
Before you can access **MySQL databases** using Python, you must install one (or more) of the following packages in a virtual environment:

* *mysqlclient*: This package contains the MySQLdb module. It is written in C, and is one of the most commonly used Python packages for MySQL.
* *mysql-connector-python*: This package contains the mysql.connector module. It is written entirely in Python.
* *PyMySQL*: This package contains the pymysql module. It is written entirely in Python.
- To install the *mysqlclient* package, type the following command:
```
        pip3 install mysqlclient
```
- To install the *mysql-connector-python* package, type the following command:
```
        pip3 install mysql-connector-python
```
- To install the *pymysql* package, type the following command:
```
        pip3 install pymysql
```
## Installing MySQL on Ubuntu
1. First, update the apt package index by typing:
```
        sudo apt update
```
2. Then install the MySQL package with the following command:
```
        sudo apt install mysql-server
```
3. To check whether the MySQL server is running, type:
```
        sudo systemctl status mysql
```
### Securing MySQL
Run the script by typing:
```
        sudo mysql_secure_installation
```
### Login as root
To log in to the MySQL server as the root user type:
```
        sudo mysql 
```
### Check user
```
        SELECT user,authentication_string,plugin,host FROM mysql.user;
```
### Change *auth_socket* plugin ==> password
```
        ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'my_password';
        FLUSH PRIVILEGES;
```
### Creat user
```
        CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';
        GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
        exit;
```
## Commandline Databse
```
        show databases;
        use demo;
        show tables;
        select *from data;
```

