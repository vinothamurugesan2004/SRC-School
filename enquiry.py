#!c:\Python\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")

print("<html>")
print("<body>")

Form=cgi.FieldStorage()
FName=Form.getvalue('name')
FEmail=Form.getvalue('email')
FPhone=Form.getvalue('Phone')
FMessage=Form.getvalue('message')

print("<h1>Your Enquiry Was Received!!!</h1>")
print(FName,FEmail,FPhone,FMessage)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="src"
)

mycursor = mydb.cursor()

sql = "INSERT INTO enquiry(Name,Email,Phone,Message)VALUES(%s,%s,%s,%s)"
val=(FName,FEmail,FPhone,FMessage)

mycursor.execute(sql,val)
mydb.commit()

print("</body>")
print("</html>")