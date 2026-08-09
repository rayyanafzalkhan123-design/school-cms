class Timetable:
    def __init__(self, day, time, classroom_number, assigned_teacher, assigned_class):
        self.day = day
        self.time = time
        self.classroom_number = classroom_number
        self.assigned_teacher = assigned_teacher
        self.assigned_class = assigned_class

    def __str__(self):
        return f"{self.day} {self.time} - Room {self.classroom_number} ({self.assigned_teacher})"