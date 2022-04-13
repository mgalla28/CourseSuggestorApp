class Course:
    """Encapsulates course information."""
    def __init__(self, course_identifier, pre_reqs=[], credit_hours=3):
        """

        :param course_identifier:
        :param pre_reqs:
        :param credit_hours:
        """
        self.course_identifier = course_identifier
        self.pre_reqs = pre_reqs
        self.credit_hours = credit_hours

    def __eq__(self, other):
        return self.course_identifier == other.course_identifier
