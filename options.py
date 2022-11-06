import mysql.connector
import sys
from pprint import pprint

#pass student classes thru command line
#convert requested courses into a map -> CType:Cnumber
courseRequests = {}
for arg in sys.argv:
    if arg=='options.py':
        continue
    c = arg.split(",")
    courseRequests[c[0]] = c[1]

mydb = mysql.connector.connect(
  host="sql.njit.edu",
  user="pk577",
  password="Data147159!!",
  port="3306",
  database="pk577"
)

mycursor = mydb.cursor()

#prepare sql for getting all requested courses
sql = "SELECT * FROM Course WHERE "
for cat in courseRequests.keys():
    sql += "CourseCat=" + cat + 
mycursor.execute(sql)

myresult = mycursor.fetchall()

#go through all courses
for course in myresult:
  print(x)
"""