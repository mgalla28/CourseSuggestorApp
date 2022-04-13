from .Course import Course
from .CourseList import CourseList
from .UniversalDataConnection import UniversalDataConnection


class Curriculum(CourseList):
    """
    CourseList that contains a graph of a given program curriculum.
    Used to compare against individual user graphs.
    """

    def __init__(self):
        dataManager = UniversalDataConnection.get_instance().data_connection
        self.course_dict = dataManager.get_courselist()

    def suggest_courses(self, user_courses: CourseList):
        courseQueue = []
        possible = []
        impossible = []

        if user_courses.course_dict == {}:  # Case when the user has no taken courses
            ret_list = []
            for course in self.course_dict.course_dict.values():
                if len(course.pre_reqs) == 0:  # should be pre reqs
                    ret_list.append(course)
            return ret_list

        for pre_req in user_courses.course_dict:
            for course in pre_req.pre_reqs:
                possible.append(course)

        for i in user_courses.course_dict.values():
            if i not in self.course_dict:
                courseQueue.append(i)

        for pre_req in courseQueue:
            for course in pre_req.pre_reqs:
                impossible.append(course)

        ret_list = []
        for course in possible:
            if course not in impossible and course not in ret_list:
                ret_list.append(course)

        return ret_list

