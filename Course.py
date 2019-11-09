class Course:
    def __init__(self, id, out_edges, credit_hours):
        self.id = id
        self.edge_list = out_edges
        self.credit_hours = credit_hours
