from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from Core import *

app = Flask(__name__)
CORS(app)
UniversalDataConnection(FileManager())
current_curriculum = Curriculum()


@app.route('/login', methods=['GET', 'POST'])
def login():
    request_json = request.get_json()
    name_query = request_json['userName']
    password = request_json['password']
    user_data = UniversalDataConnection.get_instance().data_connection.get_user(name_query)
    if user_data['password'] != password:
        abort(400)
    return jsonify({'username': user_data['username']})


@app.route('/curriculum', methods=['GET'])
def get_curriculum():
    return UniversalDataConnection.get_instance().data_connection.get_curriculum_json()


@app.route('/suggest', methods=['POST'])
def suggest_courses():
    request_json = request.get_json()
    suggested_courses = []
    if not request_json:
        suggested_courses = current_curriculum.suggest_courses(CourseList())

    else:
        course_identifier_list = []
        for val in request_json:
            course_identifier_list.append(val['course_identifier'])
        print(course_identifier_list)
        courses = current_curriculum.build_course_list(course_identifier_list)
        print(courses)
        abort(400)  # Not fully implemented

    suggested_course_list = []
    for course in suggested_courses:
        suggested_course_list.append({'course_identifier': course.course_identifier, 'credit_hours': course.credit_hours})

    return jsonify(suggested_course_list)


app.run()
