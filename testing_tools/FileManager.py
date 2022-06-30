from Core import *
from .User import User
from typing import List
import json
import os


class SingletonException(Exception):
    pass


class FileManager(DataManager):
    """Loads contents of file directly in to memory to mimic function of database."""

    def __init__(self, user_file_path: str = None, course_file_path: str = None):
        if user_file_path is None or course_file_path is None:
            path = os.getcwd()
            user_file_path = f'{path}\\data_files\\users.json' if user_file_path is None else user_file_path
            course_file_path = f'{path}\\data_files\\courses.json' if course_file_path is None else course_file_path
        user_source_file = open(user_file_path)
        course_source_file = open(course_file_path)
        self.user_json_data = json.load(user_source_file)
        self.json_data = json.load(course_source_file)

    def get_courses(self) -> Course:
        pass

    def get_user(self, user_name) -> User:
        for data in self.user_json_data.values():
            for user_data in data:
                if user_data["username"] == user_name:
                    return user_data

    def get_courselist(self) -> CourseList:
        courseDict = {}
        for data in self.json_data.values():
            for course_data in data:
                courseDict[course_data['course_identifier']] = Course(course_data['course_identifier'], course_data['pre_reqs'], course_data['credit_hours'])

        return CourseList(input_dict=courseDict)

    def get_course_json(self, course_identifier: str):
        course_list = self.json_data["courses"]
        return list(filter(lambda course: course["course_identifier"] == course_identifier, course_list))[0]

    def get_curriculum_json(self):
        return self.json_data

    def update_courses_completed(self, username: str, courses_completed: List[str]):
        pass
