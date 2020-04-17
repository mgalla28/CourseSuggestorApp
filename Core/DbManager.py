import abc
from . import User, Course, CourseList

class DbManager(abc.ABC):

    @abc.abstractmethod
    def getCourses(self) -> Course:
        pass

    @abc.abstractmethod
    def getUser(self) -> User:
        pass

    @abc.abstractmethod
    def getCourseList(self) -> CourseList:
        pass