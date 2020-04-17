from Core.CourseList import CourseList
from Core.Course import Course

from pymongo import MongoClient
import pymongo

conn = MongoClient()
db = conn.ClassGraphs
coll = db.CsClasses  # type: pymongo.collection

master_dict = {}
for i in coll.find({}):
    master_dict.update({i['designation']: Course(i['designation'], list(i['dependents']), i['credit_hours'])})


cs141 = Course('CS 141', ['CS 251', 'CS 211', 'CS 261'], 3)
cs151 = Course('CS 151', ['CS 251'], 3)
cs211 = Course('CS 211', [], 3)
cs251 = Course('CS 251', [], 3)
cs261 = Course('CS 261', [], 3)


courseDict = {'CS 141': cs141, 'CS 151': cs151, 'CS 211': cs211, 'CS 251': cs251, 'CS 261': cs261}

master = CourseList(master_dict)
user = CourseList({'CS 141': cs141})

print(master.return_vertices_set().difference(user.return_vertices_set()))