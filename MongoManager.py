from Core import *
from pymongo import MongoClient

class MongoManager(DbManager):

    def __init__(self):
        self.conn = MongoClient()
        self.db = self.conn.ClassGraphs
        self.coll = self.db.CsClasses



    def getCourses(self) -> Course:
        pass

    def getUser(self) -> User:
        pass

    def getCourseList(self) -> CourseList:
        input_dict = dict()
        for i in self.coll.find({}):
            dep_str = i['dependents']  # type: str
            dep_list = dep_str.split(",")
            input_dict[i['designation']] = Course(i['designation'], dep_list, i['credit_hours'])
        return CourseList(input_dict).return_vertices()
