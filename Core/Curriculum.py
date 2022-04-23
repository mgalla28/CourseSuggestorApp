from typing import List
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

    def build_course_list(self, course_identifier_list: List[str]) -> CourseList:
        """
        Build a list of course objects from the input list with
        the master curriculum information
        """
        new_course_list = CourseList()
        for course_identifier in course_identifier_list:
            course = self.master_course_list.course_dict[course_identifier]
            new_course_list.add_course(course)
        return new_course_list

    def suggest_courses(self, user_courses: List[str] = None) -> List[Course]:
        """
        Suggest a list of courses for next semester
        """
        suggest_list = []

        if not user_courses:  # Case when the user has no taken courses
            ret_list = []
            for course in self.master_course_list.course_dict.values():
                if not course.pre_reqs:  # should be pre reqs
                    ret_list.append(course)
            return ret_list

        for course in self.master_course_list.course_dict.values():
            if course.course_identifier in user_courses:
                continue

            pre_reqs_taken = True
            for pre_req_identifier in course.pre_reqs:
                if pre_req_identifier not in user_courses:
                    pre_reqs_taken = False

            if pre_reqs_taken:
                suggest_list.append(course)

        return suggest_list
