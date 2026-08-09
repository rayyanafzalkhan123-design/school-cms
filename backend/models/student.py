class Student:
    def __init__(self, roll_no, name, age, gender, section, gmail, major_subject):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.section = section
        self.gmail = gmail
        self.major_subject = major_subject

    def __str__(self):
        return f"{self.roll_no} - {self.name} ({self.major_subject})"