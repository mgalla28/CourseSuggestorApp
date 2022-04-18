from .Course import Course
from .CourseList import CourseList
from .UniversalDataConnection import UniversalDataConnection


class Curriculum(CourseList):
    """
    CourseList that contains a graph of a given program curriculum.
    Used to compare against individual user graphs.
    """

    def __init__(self):
        data_manager = UniversalDataConnection.get_instance().data_connection
        self.course_dict = data_manager.get_courselist()

    def build_course_list(self, course_identifier_list):
        new_course_list = CourseList()
        for course_identifier in course_identifier_list:
            course = self.course_dict.course_dict[course_identifier]
            new_course_list.add_course(course)
        return new_course_list

    def suggest_courses(self, user_courses: CourseList):
        course_queue = []
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
                course_queue.append(i)

        for pre_req in course_queue:
            for course in pre_req.pre_reqs:
                impossible.append(course)

        ret_list = []
        for course in possible:
            if course not in impossible and course not in ret_list:
                ret_list.append(course)

        return ret_list

