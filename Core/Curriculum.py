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
        self.master_course_list = data_manager.get_courselist()

    def build_course_list(self, course_identifier_list):
        new_course_list = CourseList()
        for course_identifier in course_identifier_list:
            course = self.master_course_list.course_dict[course_identifier]
            new_course_list.add_course(course)
        return new_course_list

    def suggest_courses(self, user_courses: list = None):
        course_queue = []
        possible = []
        impossible = []
        suggest_list = []

        print(user_courses)

        if not user_courses:  # Case when the user has no taken courses
            ret_list = []
            for course in self.master_course_list.course_dict.values():
                if not course.pre_reqs:  # should be pre reqs
                    ret_list.append(course)
            return ret_list

        for course in self.master_course_list.course_dict.values():
            print(course)
            if course.course_identifier in user_courses:
                continue

            pre_reqs_taken = True
            for pre_req_identifier in course.pre_reqs:
                if pre_req_identifier not in user_courses:
                    pre_reqs_taken = False

            if pre_reqs_taken:
                suggest_list.append(course)

        return suggest_list


"""
        for pre_req in user_courses.course_dict.values():
            print(pre_req)
            for course in pre_req.pre_reqs:
                print(course)
                possible.append(course)

        for i in user_courses.course_dict.values():
            print(i)
            if i.course_identifier not in self.master_course_list.course_dict:
                course_queue.append(i)

        for pre_req in course_queue:
            print(pre_req)
            for course in pre_req.pre_reqs:
                print(course)
                impossible.append(course)

        print(possible)
        print(impossible)

        ret_list = []
        for course in possible:
            if course not in impossible and course not in ret_list:
                ret_list.append(course)
"""
