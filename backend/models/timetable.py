class Timetable:
    def __init__(self, day, time, classroom_number, section, assigned_class, assigned_teacher):
        self.day = day
        self.time = time
        self.classroom_number = classroom_number
        self.section = section
        self.assigned_class = assigned_class
        self.assigned_teacher = assigned_teacher

    def __str__(self):
        return f"{self.day} {self.time} - Room {self.classroom_number} ({self.assigned_teacher})"