class Course:
    """Encapsulates course information."""
    def __init__(self, id, out_edges=[], credit_hours=3):
        self.id = id
        self.dependents = out_edges
        self.credit_hours = credit_hours

    def __eq__(self, other):
        return self.id == other.id
