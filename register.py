#!c:\Python\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")

print("<html>")
print("<body>")

Form=cgi.FieldStorage()
FName=Form.getvalue('name')
FEmail=Form.getvalue('email')
FPhone=Form.getvalue('phone')
FDateOfBirth=Form.getvalue('date')
FAddress=Form.getvalue('address')

print("<h1>Thank you for register!!!</h1>")
print(FName,FEmail,FDateOfBirth,FPhone,FAddress)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="src"
)

mycursor = mydb.cursor()

sql = "INSERT INTO student(Name,Email,DateOfBirth,Phone,Address)VALUES(%s,%s,%s,%s,%s)"
val=(FName,FEmail,FDateOfBirth,FPhone,FAddress)

mycursor.execute(sql,val)
mydb.commit()

print("</body>")
print("</html>")