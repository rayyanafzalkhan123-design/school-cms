class Classroom:
    def __init__(self, classroom_number, capacity, department, section):
        self.classroom_number = classroom_number
        self.capacity = capacity
        self.department = department
        self.section = section

    def __str__(self):
        return f"Room {self.classroom_number} - {self.department} ({self.section})"