from pymongo import MongoClient
import json

conn = MongoClient()
db = conn.CourseSuggestor
user_source_file = open('../data_files/users.json')
user_json_data = json.load(user_source_file)

user_collection = db.Users

for user_data in user_json_data.values():
    for user in user_data:
        user_collection.insert_one({
            "username": user['username'],
            "password": user['password'],
            "courses_completed": user['courses_completed'],
        })

course_source_file = open('../data_files/courses.json')
course_json_data = json.load(course_source_file)

course_collection = db.Courses

for course_data in course_json_data.values():
    for course in course_data:
        course_collection.insert_one({
            "course_identifier": course['course_identifier'],
            "pre_reqs": course['pre_reqs'],
            "credit_hours": course['credit_hours']
        })
