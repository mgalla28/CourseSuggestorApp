from typing import List

from Core import UniversalDataConnection, Course


class BackendLogicHelper:
    def __init__(self):
        self.data_connection = UniversalDataConnection.get_instance().data_connection

    def verify_login(self, user_name: str, password: str) -> bool:
        data_connection = UniversalDataConnection.get_instance().data_connection
        if not user_name:
            return False
        user_data = data_connection.get_user(user_name)
        if user_data['password'] != password:
            return False

    def get_user_courses_completed(self, user_name: str) -> List[Course]:
        courses_completed = []
        data_connection = UniversalDataConnection.get_instance().data_connection
        user_data = data_connection.get_user(user_name)
        for course_identifier in user_data['courses_completed']:
            courses_completed.append(data_connection.get_course_json(course_identifier))
        return courses_completed