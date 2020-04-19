from abc import ABC, abstractmethod
from . import User, Course, CourseList


class DataManager(ABC):

    @abstractmethod
    def get_courses(self) -> Course:
        pass

    @abstractmethod
    def get_user(self) -> User:
        pass

    @abstractmethod
    def get_courselist(self) -> CourseList:
        pass