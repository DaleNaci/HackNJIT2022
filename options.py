import mysql.connector
import sys

#pass student classes thru command line
classes=sys.argv

mydb = mysql.connector.connect(
  host="sql.njit.edu",
  user="pk577",
  password="Data147159!!",
  port="3306",
  database="pk577"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)