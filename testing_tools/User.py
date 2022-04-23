class User:
    """A user contains a unique username and a set of taken classes"""

    def __init__(self, userName, course_list=None):
        self.userName = userName
        if course_list is None:
            self.course_list = []
        else:
            self.course_list = course_list


    def suggest_courses(self, master_course_list):
        master_course_map = master_course_list

        course_queue = []
        possible = []
        impossible = []

        if self.courseSet.course_dict is False:  # Case when the user has no taken courses
            confirmed = []
            for course in master_course_map.values():
                if len(course.dependents) == 0:  # should be pre reqs
                    confirmed.append(course)
            return confirmed

        # Add anything that comes after the classes currently taken to the possible list
        for pre_req in self.courseSet.course_dict.values():
            for course in pre_req.dependents:
                possible.append(course)

        # remove currently taken classes from list if possible courses
        for course in self.courseSet.course_dict.values():
            if course.course_identifier in possible:
                possible.remove(course.course_identifier)

        # Add all untaken courses to the queue for checking
        for i in master_course_map.course_dict.values():
            if i not in self.courseSet.course_dict.values():
                course_queue.append(i)

        # Eliminate courses for which the pre reqs aren't met
        for pre_req in course_queue:
            for course in pre_req.dependents:
                impossible.append(course)

        confirmed = []
        for course in possible:
            if course not in impossible and course not in confirmed:
                confirmed.append(course)

        ret_list = []
        for course_name in confirmed:
            add_course = master_course_map.course_dict[course_name]
            ret_list.append(add_course)

        return ret_list

