from flask import Flask, request
from flask_cors import CORS
from Core import *

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    name_query = request.data.decode().replace('"', '')
    return UniversalDataConnection.get_instance().data_connection.get_user(name_query)


@app.route('/curriculum', methods=['GET'])
def get_curriculum():
    return UniversalDataConnection.get_instance().data_connection.get_courseList_json()


user_account = User(userName='guest')
UniversalDataConnection(FileManager())
app.run()
