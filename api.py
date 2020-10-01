from flask import Flask, request
from Core import *

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        return tuple('You are logged in as a guest user.', User('Guest'))


@app.route('/curriculum', methods=['GET'])
def get_curriculum():
    return UniversalDataConnection.get_instance().data_connection.get_courselist() #Need to serialize


user_account = User(userName='guest')
UniversalDataConnection(FileManager())
app.run()
