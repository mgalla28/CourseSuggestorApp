from flask import request, url_for
from flask_api import FlaskAPI
from Core import User, UniversalDataConnection, FileManager

app = FlaskAPI(__name__)

@app.route("/", methods=['GET'])
def get_all_courses():
    """
    Loads data in right box

    :return: List of courses
    """
    return UniversalDataConnection.get_instance().get_courses()


@app.route("/", methods=['GET', 'PUT'])
def user_courses():
    """
    Get or add user courses

    :return:
    """
    if request.method == 'GET':
        return user_account.courseSet
    elif request.method == 'PUT':
        pass #TODO: How the h*ck am I going to handle the put and the get? Need to get argument




if __name__ == "__main__":
    user_account = User(userName='guest')
    UniversalDataConnection(data_manager=FileManager)
    app.run()
