from flask import Flask, request
from flask_cors import CORS
from Core import *

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        return 'You are logged in as a guest user.', User('Guest')


@app.route('/curriculum', methods=['GET'])
def get_curriculum():
    return UniversalDataConnection.get_instance().data_connection.get_courseList_json()  # Need to serialize

user_account = User(userName='guest')
UniversalDataConnection(FileManager())
app.run()
