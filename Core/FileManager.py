from Core import *
import json
import os


class SingletonException(Exception):
    pass


class FileManager(DataManager):
    """Loads contents of file directly in to memory to mimic function of database."""

    def __init__(self):
        path = os.getcwd()
        user_source_file = open('data_files\\users.json')
        course_source_file = open(f'{path}\\data_files\\courses.json')
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

    def get_courseList_json(self):
        return self.json_data
