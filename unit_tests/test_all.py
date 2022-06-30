from Core import UniversalDataConnection
from testing_tools.FileManager import FileManager
from pathlib import Path

def test_data_connection():
    currentProjPath = Path.cwd().parent
    user_file_path = f'{currentProjPath}\\data_files\\users.json'
    courses_file_path = f'{currentProjPath}\\data_files\\courses.json'

    UniversalDataConnection(FileManager(user_file_path=user_file_path, course_file_path=courses_file_path))
    data_connection = UniversalDataConnection.get_instance().data_connection
    course_json = data_connection.get_course_json("CS 141")

    assert course_json["course_identifier"] == "CS 141"
