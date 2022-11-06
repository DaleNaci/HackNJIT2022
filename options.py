import sys
import itertools

from pprint import pprint
import mysql.connector

from data.helper_functions import check_conflict
from data.components.section import Section


def main():
    x = get_combination()

    for t in x:
        print(t[0].crn, t[1].crn, t[2].crn)


def get_combination():
    courseRequests = []
    for arg in sys.argv[1:]:
        c = arg.split(",")
        courseRequests.append((c[0],c[1]))

    with open("db_password.txt", "r") as f:
        mydb = mysql.connector.connect(
            host = "sql.njit.edu",
            user = "pk577",
            password = f.readline().strip(),
            port = "3306",
            database = "pk577"
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

    return list(itertools.product(*courses))



if __name__ == "__main__":
    main()