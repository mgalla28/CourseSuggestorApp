from Core import *
from pymongo import MongoClient


class SingletonException(Exception):
    pass


class MongoManager(DataManager):
    """DataManager for MongoDB connections"""
    def __init__(self):
        self.conn = MongoClient('mongodb:27017')
        self.db = self.conn.CourseSuggestor
        self.users = self.db.Users
        self.courses = self.db.Courses

    def create_user(self, user_name: str, password: str) -> None:
        self.users.insert_one({'username': user_name, 'password': password, 'courses_completed': []})

    def get_courselist(self) -> CourseList:
        all_courses = self.courses.find({})
        course_dict = {}
        for data in all_courses:
            course_dict[data['course_identifier']] = Course(data['course_identifier'],
                                                           data['pre_reqs'],
                                                           data['credit_hours'])
        return CourseList(input_dict=course_dict)

    def get_user(self, user_name):
        username_match = self.users.find_one({'username': user_name})
        return username_match

    def get_course_json(self, course_identifier):
        course = self.courses.find_one({'course_identifier': course_identifier}, {'_id': False})
        return course

    def get_curriculum_json(self):
        all_courses = self.courses.find({})
        all_courses = [{'course_identifier': c['course_identifier'], 'pre_reqs': c['pre_reqs'], 'credit_hours': c['credit_hours']} for c in all_courses]
        courses_json = {'courses': all_courses}
        return courses_json

    def update_courses_completed(self, username, courses_completed):
        current_completed_courses = self.users.find_one({'username': username}, {'_id': False, 'username': False, 'password': False})
        courses_completed.extend(current_completed_courses['courses_completed'])
        courses_completed.sort()

        self.users.update_one({'username': username}, {'$set': {'courses_completed': courses_completed}})
        response = self.users.find_one({'username': username}, {'_id': False, 'username': False, 'password': False})
        return response  # Get the new updated list of courses taken by user
