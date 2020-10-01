from Core import *
from pymongo import MongoClient
import json
import os


class SingletonException(Exception):
    pass


class FileManager(DataManager):
    """Loads contents of file directly in to memory to mimic function of database."""

    def __init__(self):
        path = os.getcwd()
        source_file = open(f'{path}\\data_files\\courses.json')
        self.json_data = json.load(source_file)

    def get_courses(self) -> Course:
        pass

    def get_user(self) -> User:
        pass

    def get_courselist(self) -> CourseList:
        courseDict = {}
        for data in self.json_data.values():
            for course_data in data:
                courseDict[course_data['course_identifier']] = Course(course_data['course_identifier'], course_data['dependents'], course_data['credit_hours'])

        return CourseList(input_dict=courseDict)
