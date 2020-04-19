from .Course import Course
from .CourseList import CourseList

class SingletonException(Exception):
    pass


class Curriculum(CourseList):
    '''
    Singleton CourseList that contains a graph of a given program curriculum.
    Used to compare against individual user graphs.
    '''

    __instance = None

    def __init__(self):
        if Curriculum.__instance is not None:
            raise SingletonException()

        else:

            cs141 = Course('CS 141', ['CS 251', 'CS 211', 'CS 261'], 3)
            cs151 = Course('CS 151', ['CS 251'], 3)
            cs211 = Course('CS 211', [], 3)
            cs251 = Course('CS 251', [], 3)
            cs261 = Course('CS 261', [], 3)

            courseDict = {'CS 141': cs141, 'CS 151': cs151, 'CS 211': cs211, 'CS 251': cs251, 'CS 261': cs261}
            newCurriculum = CourseList(input_dict=courseDict)  # TODO: Have a database collection that just contains the master list for access
            Curriculum.__instance = newCurriculum

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Curriculum.__instance == None:
            Curriculum()
        return Curriculum.__instance

    def suggest_courses(self, user_courses: CourseList):
        courseQueue = []
        possible = []
        impossible = []

        if user_courses.course_dict is False:  # Case when the user has no taken courses
            ret_list = []
            for course in self.course_dict.values:
                if len(course.dependents) == 0:  # should be pre reqs
                    ret_list.append(course)
            return ret_list

        for pre_req in user_courses.course_dict:
            for course in pre_req.dependents:
                possible.append(course)

        for i in user_courses.course_dict.values():
            if i not in self.course_dict:
                courseQueue.append(i)

        for pre_req in courseQueue:
            for course in pre_req.dependents:
                impossible.append(course)

        ret_list = []
        for course in possible:
            if course not in impossible and course not in ret_list:
                ret_list.append(course)

        return ret_list

