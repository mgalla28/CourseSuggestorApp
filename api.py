from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from Core import *
from MongoManager import MongoManager
from BackendLogicHelper import BackendLogicHelper

app = Flask(__name__)
CORS(app)
UniversalDataConnection(MongoManager())
current_curriculum = Curriculum()
backend_logic_helper = BackendLogicHelper()




@app.route('/login', methods=['GET', 'POST'])
def login():
    request_json = request.get_json()
    user_name = request_json['userName']
    if not backend_logic_helper.verify_login(user_name=user_name, password=request_json['password']):
        abort(400)

    courses_completed = backend_logic_helper.get_user_courses_completed(user_name=user_name)
    return jsonify({'username': user_name, 'courses_completed': courses_completed})


@app.route('/curriculum', methods=['GET'])
def get_curriculum():
    return UniversalDataConnection.get_instance().data_connection.get_curriculum_json()


@app.route('/complete_courses', methods=['POST'])
def complete_courses():
    request_json = request.get_json()
    username = request_json['user_name']
    completed_courses = request_json['courses']

    data_connection = UniversalDataConnection.get_instance().data_connection
    new_completed_courses = data_connection.update_courses_completed(username, completed_courses)
    new_course_list = current_curriculum.build_course_list(new_completed_courses['courses_completed'])
    ret_list = []
    for course in new_course_list.course_dict.values():
        ret_list.append({'course_identifier': course.course_identifier, 'credit_hours': course.credit_hours})
    return jsonify(ret_list)


@app.route('/suggest', methods=['POST'])
def suggest_courses():
    request_json = request.get_json()
    if not request_json:
        suggested_courses = current_curriculum.suggest_courses()

    else:
        course_identifier_list = []
        for val in request_json:
            course_identifier_list.append(val['course_identifier'])
        suggested_courses = current_curriculum.suggest_courses(course_identifier_list)

    suggested_course_list = []
    for course in suggested_courses:
        suggested_course_list.append({'course_identifier': course.course_identifier, 'credit_hours': course.credit_hours})

    return jsonify(suggested_course_list)


app.run()
