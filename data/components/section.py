from random import randint


class Section:
    def __init__(self, course_category, course_number, course_name, crn, professor_name):
        self.course_category = course_category
        self.course_number = course_number
        self.course_name = course_name
        self.crn = crn
        self.professor_name = professor_name
        self.rmp = randint(1, 5) # Usually would grab from database
        self.periods = []


    def time_conflict(self, other_section) -> bool:
        for myp in self.periods:
            my_day, my_time = myp

            for otherp in other_section.periods:
                other_day, other_time = otherp

                if my_day != other_day:
                    continue

                my_time_start, my_time_end = self.__time_split(my_time)
                other_time_start, other_time_end = self.__time_split(other_time)

                if self.__army(my_time_start) <= self.__army(other_time_start) <= self.__army(my_time_end):
                    return True
                
                if self.__army(my_time_start) <= self.__army(other_time_end) <= self.__army(my_time_end):
                    return True

        return False


    def __time_split(self, s: str) -> tuple[str, str]:
        return s.split(" - ")


    def __army(self, s: str) -> int:
        hour = int(s.split(":")[0])
        minute = int(s.replace(":", " ").split(" ")[1])
        meridian = s[-2:]
        
        if hour == 12:
            hour = 0
        if meridian == "PM":
            hour += 12
        
        return hour * 100 + minute