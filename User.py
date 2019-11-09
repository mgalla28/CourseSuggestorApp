class User:
    """A user contains a unique username and a set of taken classes"""

    def __init__(self, userName, courseSet=None):
        self.userName = userName
        self.courseSet = courseSet
