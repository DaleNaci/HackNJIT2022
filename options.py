import mysql.connector
import sys
from pprint import pprint
from data.helper_functions import check_conflict

import itertools


class Section:
    def __init__(self, course_category, course_number, course_name, crn, professor_name):
        self.course_category = course_category
        self.course_number = course_number
        self.course_name = course_name
        self.crn = crn
        self.professor_name = professor_name
        self.start = None
        self.end = None


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
    sql = "SELECT C.CourseCat, C.Number, C.Name, S.CRN, S.ProfessorName FROM Course as C, Section as S WHERE ("
    sql += "C.CourseCat=\"" + cat + "\" AND C.Number=\"" + num + "\" AND C.CourseId=S.CourseId)"
    mycursor.execute(sql)
    # courses.append(mycursor.fetchall())
    sections = []

    for section_info in mycursor.fetchall():
        sections.append(Section(section_info[0], section_info[1], section_info[2], section_info[3], section_info[4]))

    courses.append(sections)

x = list(itertools.product(*courses))

for t in x:
    print(t[0].crn, t[1].crn, t[2].crn)