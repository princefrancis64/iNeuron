import mysql.connector as connection

mydb = connection.connect(host = "localhost" ,user = "root", passwd = "Letsgo1247")
cursor = mydb.cursor()
# cursor.execute("create database prince")
# cursor.execute("show databases")
# q1 = cursor.execute("create table prince.ineuron(employee_id int(10),emp_name varchar(80),emp_mailid varchar(20),emp_salary int(6),emp_attendance int(3))")
# print(cursor.fetchall())
q2 = cursor.execute("select * from prince.ineuron")
print(q2)
