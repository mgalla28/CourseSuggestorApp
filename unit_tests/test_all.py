from Core import UniversalDataConnection
from testing_tools.FileManager import FileManager
from pathlib import Path
import pytest
from BackendLogicHelper import BackendLogicHelper

@pytest.fixture
def user_file_path():
    currentProjPath = Path.cwd().parent
    yield currentProjPath / 'data_files' / 'users.json'

@pytest.fixture()
def courses_file_path():
    currentProjPath = Path.cwd().parent
    yield currentProjPath / 'data_files' / 'courses.json'

def test_data_connection(courses_file_path):
    UniversalDataConnection(FileManager(course_file_path=courses_file_path))
    data_connection = UniversalDataConnection.get_instance().data_connection
    course_json = data_connection.get_course_json("CS 141")

    assert course_json["course_identifier"] == "CS 141"

def test_verify_login(user_file_path, courses_file_path):
    UniversalDataConnection(FileManager(user_file_path=user_file_path, course_file_path=courses_file_path))
    backend_logic_helper = BackendLogicHelper()
    login_verified = backend_logic_helper.verify_login(user_name='Guest', password='')

    assert login_verified
