import mysql.connector as connection

mydb = connection.connect(host = "localhost" ,user = "root", passwd = "Letsgo1247")
cursor = mydb.cursor()
cursor.execute("select employee_id,emp_mailid from prince.ineuron")
for i in cursor.fetchall():
    print(i,list(i))