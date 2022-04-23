from .Course import Course
from collections import OrderedDict

class CourseList:
    """Graph that contains courses."""

    def __init__(self, input_dict: dict = None):
        if input_dict is not None:
            self.course_dict = OrderedDict(sorted(input_dict.items(), reverse=True))
        else:
            self.course_dict = OrderedDict()

    def return_vertices(self):
        ret_lst = []
        for i in self.course_dict.keys():
            ret_lst.append(i)
        return ret_lst

    def return_vertices_set(self):
        ret_set = set()
        for key, value in self.course_dict.items():
            ret_set.add(key)
        return ret_set

    def add_course(self, course):
        if type(course) is Course and course.course_identifier not in self.course_dict:
            self.course_dict[course.course_identifier] = course
            self.course_dict = OrderedDict(sorted(self.course_dict.items(), reverse=True))
