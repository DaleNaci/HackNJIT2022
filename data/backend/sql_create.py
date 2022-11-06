import os
import random

import mysql.connector
from bs4 import BeautifulSoup
from pprint import pprint


def parse_spreadsheets():
    x = 0
    path = "../../resources/course_spreadsheets"
    file_names = os.listdir(path)

    course_directory = []

    for fn in file_names:
        x += 1
        file_path = f"{path}/{fn}"

        with open(file_path, "r") as f:
            soup = BeautifulSoup(f, "html.parser")
        
        count = 0
        class_directory = {"sections": [], "category_name": fn.split(".")[-2]}
        section_info = {}

        for t in soup.find_all():
            if not t.has_attr("ng-bind-html"):
                continue

            s = t.text.strip().replace("'", "")

            if t.name == "div":
                count = 0
                if section_info:
                    class_directory["sections"].append(section_info)
                section_info = {}
                if class_directory["sections"]:
                    course_directory.append(class_directory)
                class_directory = {
                    "sections": [],
                    "category_name": fn.split(".")[-2].upper(),
                    "course_number": s.split()[1]
                }
                class_directory["name"] = s

            if count == 0:
                class_directory["name"] = s
            if count % 12 == 1:
                if section_info:
                    class_directory["sections"].append(section_info)
                section_info = {}
                section_info["section_number"] = s
            if count % 12 == 2:
                section_info["CRN"] = s
            if count % 12 == 4:
                section_info["day"] = s
            if count % 12 == 5:
                section_info["time"] = s
            if count % 12 == 10:
                section_info["professor"] = s

            # DON'T DELETE THIS COMMENT, VERY IMPORTANT JUST IN CASE
            # print(f"{count}\t{t.text}")

            count += 1

        # if x > 3:        
        #     break
    
    return course_directory


def add_to_db(course_directory):
    with open("../../db_password.txt", "r") as f:
        mydb = mysql.connector.connect(
            host = "sql.njit.edu",
            user = "pk577",
            password = f.readline().strip(),
            port = "3306",
            database = "pk577"
        )

    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Course WHERE 1")
    cursor.execute("DELETE FROM Section WHERE 1")
    cursor.execute("DELETE FROM Professor WHERE 1")
    cursor.execute("DELETE FROM Meet WHERE 1")

    course_id_counter = -1
    meet_id_counter = -1

    for course in course_directory:
        course_terms = []  # CourseId, CourseCat, Number, Name
        section_terms = []  #  CRN, CourseId, ProfessorName
        professor_terms = []  # name, Rating
        meet_terms = []  # MeetId, CRN, Day, Time

        course_id_counter += 1
        course_terms = [
                course_id_counter,
                course["category_name"],
                course["course_number"],
                course["name"]
        ]

        print(course_terms)

        cursor.execute(f"""
            INSERT INTO Course
                 VALUES ({course_terms[0]}, '{course_terms[1]}', '{course_terms[2]}', '{course_terms[3]}')
        """)

        for section in course["sections"]:
            section_terms = [
                section["CRN"],
                course_id_counter,
                section["professor"]
            ]

            professor_terms = [
                section["professor"],
                get_rmp_value(section["professor"])
            ]

            cursor.execute(f"""
                INSERT INTO Section
                     VALUES ({section_terms[0]}, {section_terms[1]}, '{section_terms[2]}')
            """)

            cursor.execute(f"""
                INSERT IGNORE INTO Professor
                            VALUES ('{professor_terms[0]}', {professor_terms[1]})
            """)

            days = [c for c in section["day"]]
            times = []

            if len(section["time"]) > 20 and section["time"][:19] != section["time"][19:]:
                times = [
                    section["time"][:19],
                    section["time"][19:]
                ]
            elif len(section["time"]) > 20:
                time = [section["time"][:19]]
            else:
                times = [section["time"]]
            
            for day in days:
                for time in times:
                    meet_id_counter += 1
                    meet_terms = [
                        meet_id_counter,
                        section["CRN"],
                        day,
                        time
                    ]

                    cursor.execute(f"""
                        INSERT IGNORE INTO Meet
                                    VALUES ({meet_terms[0]}, {meet_terms[1]}, '{meet_terms[2]}', '{meet_terms[3]}')
                    """)
            
            
    mydb.commit()


def get_rmp_value(professor_name):
    return random.randint(1, 5)


def main():
    course_directory = parse_spreadsheets()
    add_to_db(course_directory)


if __name__ == "__main__":
    main()