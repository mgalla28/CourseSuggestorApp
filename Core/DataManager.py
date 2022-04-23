from abc import ABC, abstractmethod
from typing import List

from . import CourseList


class DataManager(ABC):
    """
    Abstract base class that defines the methods needed
    to work with the data source
    """

    @abstractmethod
    def get_user(self, user_name: str) -> dict:
        """
        Get user data
        """
        pass

    @abstractmethod
    def get_courselist(self) -> CourseList:
        """
        Get all courses in storage
        """
        pass

    @abstractmethod
    def get_course_json(self, course_identifier: str) -> dict:
        """
        Get json for individual course
        """
        pass

    @abstractmethod
    def get_curriculum_json(self) -> dict:
        """
        Get all courses in storage as JSON
        """
        pass

    @abstractmethod
    def update_courses_completed(self, username: str, courses_completed: List[str]) -> dict:
        """
        Update the courses completed for a user and return the updated list
        """
        pass
