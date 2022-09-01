from typing import List

from Core import UniversalDataConnection, Course
from passlib.hash import sha256_crypt


class BackendLogicHelper:
    def __init__(self):
        self.data_connection = UniversalDataConnection.get_instance().data_connection

    def verify_login(self, user_name: str, password: str) -> bool:
        data_connection = UniversalDataConnection.get_instance().data_connection
        if not user_name:
            return False
        user_data = data_connection.get_user(user_name)
        if not sha256_crypt.verify(password, user_data['password']):
            return False

        return True

    def get_user_courses_completed(self, user_name: str) -> List[Course]:
        courses_completed = []
        data_connection = UniversalDataConnection.get_instance().data_connection
        user_data = data_connection.get_user(user_name)
        for course_identifier in user_data['courses_completed']:
            courses_completed.append(data_connection.get_course_json(course_identifier))
        return courses_completed

    def update_user_completed_courses(self, user_name, courses, current_curriculum):
        data_connection = UniversalDataConnection.get_instance().data_connection
        new_completed_courses = data_connection.update_courses_completed(user_name, courses)
        new_course_list = current_curriculum.build_course_list(new_completed_courses['courses_completed'])
        updated_course_list = []
        for course in new_course_list.course_dict.values():
            updated_course_list.append({'course_identifier': course.course_identifier, 'credit_hours': course.credit_hours})
        
        return updated_course_list
