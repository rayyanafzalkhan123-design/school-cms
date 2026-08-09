class Teacher:
    def __init__(self, id, name, gender, subject, specialization):
        self.id = id
        self.name = name
        self.gender = gender
        self.subject = subject
        self.specialization = specialization

    def __str__(self):
        return f"{self.id} - {self.name} ({self.subject})"