import sys
import itertools

from pprint import pprint
import mysql.connector

from helper_functions import check_conflict
from components.section import Section


def main():
    course_lst = get_sections()

    #connect to mysql
    with open("../db_password.txt", "r") as f:
        mydb = mysql.connector.connect(
            host = "sql.njit.edu",
            user = "pk577",
            password = f.readline().strip(),
            port = "3306",
            database = "pk577"
        )
        mycursor = mydb.cursor()
        for section_lst in course_lst:
            for section in section_lst:
                #add date and time to section periods
                sql = "SELECT Day, Time FROM Meet WHERE CRN=\"" + str(section.crn) + "\""
                mycursor.execute(sql)
                section.periods = mycursor.fetchall()

    allCombos = get_combination(course_lst)
    # pprint(allCombos)
    #loop through x "cobinations of courses"
    #test each element against the others
    goodCombos = remove_conflicts(allCombos)

    evaluate_options(goodCombos)


def evaluate_options(goodCombos):
    six_to_nine = int(sys.argv[1])
    eight_thirty = int(sys.argv[2])
    monday = int(sys.argv[3])
    friday = int(sys.argv[4])
    rmp = int(sys.argv[5])

    ratings = []

    for combo in goodCombos:
        rr = 0

        if six_to_nine > 0:
            good = True

            for section in combo: #Double check sections are in combos
                for period in section.periods:
                    if period[1] == "6:00 PM - 8:50 PM":
                        good = False
                        break
        
            if good:
                rr += six_to_nine
        
        if eight_thirty > 0:
            good = True

            for section in combo:
                for period in section.periods:
                    if period[1] == "6:00 PM - 8:50 PM":
                        good = False
                        break
            
            if good:
                rr += eight_thirty
        
        if monday > 0:
            good = True

            for section in combo:
                for period in section.periods:
                    if period[0] == "M":
                        good = False
                        break
            
            if good:
                rr += monday
        
        if friday > 0:
            good = True

            for section in combo:
                for period in section.periods:
                    if period[0] == "F":
                        good = False
            
            if good:
                rr += friday
            
        if rmp > 0:
            total_rmp = 0

            for section in combo:
                total_rmp += section.rmp
            
            rr += (total_rmp / 25) * rmp

        ratings.append((rr, combo))

    ratings.sort(key = lambda ratings: ratings[0], reverse=True)

    x = 0

    for t in ratings:
        x += 1
        if x > 5:
            break
        s = str(round(t[0], 2))
        s += " "

        for section in t[1]:
            s += section.course_category
            s += " "
            s += section.course_number
            if section != t[1][-1]:
                s += ", "

        print(s)



def remove_conflicts(allCombos):
    goodCombos = []
    for combo in allCombos:
        clen = len(combo)
        good = True #does combo work
        #compare all elements in combo for t conflict
        for i in range(clen):
            for j in range(i+1,clen):
                if(combo[i].time_conflict(combo[j])):
                    #Detect time conflict and break out
                    good = False
                    break
            if good == False:
                break
        if good == True:
            goodCombos.append(combo)
    
    return goodCombos


def get_sections():
    courseRequests = []
    for arg in sys.argv[6:]:
        c = arg.split(",")
        courseRequests.append((c[0],c[1]))

    with open("../db_password.txt", "r") as f:
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
    
    return courses


def get_combination(courses):
    return list(itertools.product(*courses))


main()