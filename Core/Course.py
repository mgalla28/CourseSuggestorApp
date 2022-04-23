from typing import List


class Course:
    """Encapsulates course information."""

    def __init__(self, course_identifier, pre_reqs: List[str] = None, credit_hours: int = 3):
        """
        :param course_identifier: Identifier string for course
        :param pre_reqs: List of identifier strings for pre requisite courses
        :param credit_hours: Number of credit hours for course
        """
        self.course_identifier = course_identifier
        if pre_reqs is None:
            self.pre_reqs = []
        else:
            self.pre_reqs = pre_reqs
        self.credit_hours = credit_hours

    def __eq__(self, other):
        return self.course_identifier == other.course_identifier

    def __repr__(self):
        return f'Course object with identifier of {self.course_identifier}'
