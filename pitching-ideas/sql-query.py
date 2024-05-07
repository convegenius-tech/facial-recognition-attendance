import mysql.connector


conn=mysql.connector.connect(host="localhost",username="root",password="sumit@123",database="sumitdb")
my_cursor=conn.cursor()
my_cursor.execute("select * from student1")
myresult=my_cursor.fetchall()
print(myresult)


conn.commit()

conn.close()