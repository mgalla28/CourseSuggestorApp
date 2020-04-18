class Course:
    """Encapsulates course information."""
    def __init__(self, course_identifier, out_edges=[], credit_hours=3):
        """

        :param course_identifier:
        :param out_edges:
        :param credit_hours:
        """
        self.course_identifier = course_identifier
        self.dependents = out_edges
        self.credit_hours = credit_hours

    def __eq__(self, other):
        return self.course_identifier == other.course_identifier
