import mysql.connector as conn

mydb = conn.connect(host = "localhost",user = "root",passwd = "Letsgo1247")
cursor = mydb.cursor()
cursor.execute("create database prince")
cursor.execute("show databases")
cursor.execute("create table prince.ineuron(emp_id int(10),emp_name varchar(30),emp_emailid varchar(30),emp_salary int(30),empl_attendance varchar(30))")
print(cursor.fetchall())
q2 = cursor.execute("select * from prince.ineuron")
print(q2)


cursor.execute("insert into prince.ineuron values(101,'prince francis','prince.francis.google',100,30)")
mydb.commit()
cursor.execute("select * from prince.ineuron")
for i in cursor.fetchall():
    print(i)

cursor.execute("select employee_id,emp_emailid from prince.ineuron")
for i in cursor.fetchall():
    print(i)
