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
courses = []
sql = "SELECT * FROM Course as C, Section as S, Meet as M WHERE ("
for cat in courseRequests.keys():
    sql += "C.CourseCat=\"" + cat + "\" AND C.Number=\"" + courseRequests[cat] + "\" AND C.CourseId=S.CourseId AND S.CRN=M.CRN)"
    mycursor.execute(sql)
    courses.append(mycursor.fetchall())

pprint(courses)
  