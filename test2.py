import mysql.connector as connection

mydb = connection.connect(host = "localhost" ,user = "root", passwd = "Letsgo1247")
cursor = mydb.cursor()
# cursor.execute("insert into prince.ineuron values(101,'prince','prince.francis64',100,30)")
# mydb.commit()
cursor.execute("select * from prince.ineuron")
for i in cursor.fetchall():
    print(i)