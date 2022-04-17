from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from Core import *

app = Flask(__name__)
CORS(app)


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


UniversalDataConnection(FileManager())
app.run()
