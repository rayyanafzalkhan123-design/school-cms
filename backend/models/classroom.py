class Classroom:
    def __init__(self, classroom_number, capacity, department):
        self.classroom_number = classroom_number
        self.capacity = capacity
        self.department = department

    def __str__(self):
        return f"Room {self.classroom_number} - {self.department}"