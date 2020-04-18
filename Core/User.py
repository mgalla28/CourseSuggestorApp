from Core import Course, CourseList

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