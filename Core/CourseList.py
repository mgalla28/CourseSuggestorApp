from Core.Course import Course

class CourseList:
    """Graph that contains courses."""
    def __init__(self, input_dict: dict = None):
        self.course_dict = {}
        if input_dict is not None:
            print(f'This is input dict {input_dict}')
            for key, value in input_dict.items():
                self.course_dict[key] = value

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
        if type(course) is Course:
            self.course_dict[course.course_identifier] = course

    def suggest_courses(self):
        pass







