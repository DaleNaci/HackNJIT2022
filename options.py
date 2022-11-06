import mysql.connector
import sys
from pprint import pprint
from data.helper_functions import check_conflict

#pass student classes thru command line
#convert requested courses into a map -> CType:Cnumber
courseRequests = []
for arg in sys.argv[1:]:
    c = arg.split(",")
    courseRequests.append((c[0],c[1]))

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
for cat, num in courseRequests:
    sql = "SELECT * FROM Course as C, Section as S, Meet as M WHERE ("
    sql += "C.CourseCat=\"" + cat + "\" AND C.Number=\"" + num + "\" AND C.CourseId=S.CourseId AND S.CRN=M.CRN)"
    mycursor.execute(sql)
    courses.append(mycursor.fetchall())

#info for each course
#[(0:CourseId, 1:CourseCat, 2:CourseNum, 3:CourseName, 4:CRN, 5:CourseId, 
# 6:ProfessorName, 7:MeetId, 8:CRN, 9:Day, 10:Time)]

#get number of sections for each course
for course in courses:
    crns = []
    #add section number attribute as first element
    course.insert(0, 0)
    for possibleSection in course[1:]:
        if course[4] not in crns:
            crns.append()

#make combos
combos = []
#get total combos
total = 0
for course in courses:
    total *= 
for course in courses:
    for section in course:
        for otherSections in combos:

            if check_conflict(section[9], section[10], ):
                combos.append(section)
