from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from Core import *
from MongoManager import MongoManager
from BackendLogicHelper import BackendLogicHelper
from swagger_ui import api_doc

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

    updated_user_course_list = backend_logic_helper.update_user_completed_courses(user_name=username,
                                                                                  courses=completed_courses,
                                                                                  current_curriculum=current_curriculum)
    return jsonify(updated_user_course_list)


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
        suggested_course_list.append(
            {'course_identifier': course.course_identifier, 'credit_hours': course.credit_hours})

    return jsonify(suggested_course_list)


spec_file = open('static/swagger.json').read()
api_doc(app, config_spec=spec_file, url_prefix='/spec', title='Api Doc')
app.run()
