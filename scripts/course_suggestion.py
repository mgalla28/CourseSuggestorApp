from Core.CourseList import CourseList
from Core.Course import Course

from pymongo import MongoClient
import pymongo

conn = MongoClient()
db = conn.ClassGraphs
coll = db.CsClasses  # type: pymongo.collection

master_dict = {}
for i in coll.find({}):
    dep_str = i['dependents'] # type: str
    dep_list = dep_str.split(",")
    master_dict.update({i['designation']: Course(i['designation'], dep_list, i['credit_hours'])})


cs141 = Course('CS141', ['CS251', 'CS211', 'CS261'], 3)
cs151 = Course('CS151', ['CS251'], 3)
cs211 = Course('CS211', [], 3)
cs251 = Course('CS251', [], 3)
cs261 = Course('CS261', [], 3)


courseDict = {'CS141': cs141, 'CS151': cs151, 'CS211': cs211, 'CS251': cs251, 'CS261': cs261}

master = CourseList(master_dict)
user = CourseList({'CS 141': cs141})



def suggest_courses(masterList: CourseList, courses: [Course] = None) -> [Course]:
    courseQueue = []
    possible = []
    impossible = []

    if courses is None:  # Case when the user has no taken courses
        ret_list = []
        for course in masterList.course_dict.values:
            if len(course.dependents) == 0: # should be pre reqs
                ret_list.append(course)
        return ret_list

    for pre_req in courses:
        for course in pre_req.dependents:
            possible.append(course)

    for i in masterList.course_dict.values():
        if i not in courses:
            courseQueue.append(i)

    for pre_req in courseQueue:
        for course in pre_req.dependents:
            impossible.append(course)

    ret_list = []
    for course in possible:
        if course not in impossible and course not in ret_list:
            ret_list.append(course)

    return ret_list


print(suggest_courses(master, [cs141]))
print(suggest_courses(master, [cs141, cs151]))



