from pymongo import MongoClient
import json

conn = MongoClient()
db = conn.CourseSuggestor

course_source_file = open('data_files/courses.json')
course_json_data = json.load(course_source_file)

course_collection = db.Courses

for course_data in course_json_data.values():
    for course in course_data:
        course_collection.update_one({"course_identifier": course["course_identifier"]}, {"$set": course})
