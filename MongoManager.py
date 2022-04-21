from Core import *
from pymongo import MongoClient


class SingletonException(Exception):
    pass


class MongoManager(DataManager):
    '''DataManager for MongoDB connections'''
    def __init__(self):
        self.conn = MongoClient()
        self.db = self.conn.CourseSuggestor
        self.users = self.db.Users
        self.courses = self.db.Courses

    def get_courses(self) -> Course:
        pass

    def get_courselist(self) -> CourseList:
        all_courses = self.courses.find({})
        courseDict = {}
        for data in all_courses:
            courseDict[data['course_identifier']] = Course(data['course_identifier'],
                                                           data['pre_reqs'],
                                                           data['credit_hours'])

        return CourseList(input_dict=courseDict)

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
