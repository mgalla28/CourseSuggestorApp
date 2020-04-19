from Core import Course, CourseList
from Core.UniversalDataConnection import UniversalDataConnection

class User:
    """A user contains a unique username and a set of taken classes"""

    def __init__(self, userName, courseSet: CourseList=None):
        self.userName = userName
        if courseSet is None:
            self.courseSet = CourseList()
        else:
            self.courseSet = courseSet

    def add_course(self, course):
        self.courseSet.add_course(course)

    def suggest_courses(self):
        master_course_map = UniversalDataConnection.get_instance().data_connection.get_courselist()

        courseQueue = []
        possible = []
        impossible = []

        if self.courseSet.course_dict is False:  # Case when the user has no taken courses
            ret_list = []
            for course in master_course_map.values:
                if len(course.dependents) == 0:  # should be pre reqs
                    ret_list.append(course)
            return ret_list

        # Add anything that comes after the classes currently taken to the possible list
        for pre_req in self.courseSet.course_dict.values():
            for course in pre_req.dependents:
                possible.append(course)

        # Add all untaken courses to the queue for checking
        for i in master_course_map.course_dict.values():
            if i not in self.courseSet.course_dict.values():
                courseQueue.append(i)

        # Eliminate courses for which the pre reqs aren't met
        for pre_req in courseQueue:
            for course in pre_req.dependents:
                impossible.append(course)

        ret_list = []
        for course in possible:
            if course not in impossible and course not in ret_list:
                ret_list.append(course)

        return ret_list