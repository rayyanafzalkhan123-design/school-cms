from fastapi import FastAPI
from models.student_db import add_student, get_students, delete_student, search_student
from models.teacher_db import add_teacher, get_teachers, delete_teacher, search_teacher
from models.classroom_db import add_classroom, get_classrooms, delete_classroom, search_classroom
from models.timetable_db import add_timetable, get_timetable, delete_timetable, search_timetable

app = FastAPI()

@app.get("/students")
def read_students():
    return get_students()

@app.post("/students")
def create_student(roll_no: str, name: str, age: int, gender: str, section: str, gmail: str, major_subject: str):
    add_student(roll_no, name, age, gender, section, gmail, major_subject)
    return {"message": "Student added"}

@app.get("/teachers")
def read_teachers():
    return get_teachers()

@app.post("/teachers")
def create_teacher(id: str, name: str, gender: str, subject: str, specialization: str):
    add_teacher(id, name, gender, subject, specialization)
    return {"message": "Teacher added"}

@app.get("/classrooms")
def read_classrooms():
    return get_classrooms()

@app.post("/classrooms")
def create_classroom(classroom_number: str, capacity: int, department: str):
    add_classroom(classroom_number, capacity, department)
    return {"message": "Classroom added"}

@app.get("/timetable")
def read_timetable():
    return get_timetable()

@app.post("/timetable")
def create_timetable(day: str, time: str, classroom_number: str, assigned_teacher: str, assigned_class: str):
    add_timetable(day, time, classroom_number, assigned_teacher, assigned_class)
    return {"message": "Timetable entry added"}

@app.get("/students/{roll_no}")
def find_student(roll_no: str):
    return search_student(roll_no)

@app.delete("/students/{roll_no}")
def remove_student(roll_no: str):
    delete_student(roll_no)
    return {"message": "Student deleted"}

@app.get("/teachers/{id}")
def find_teacher(id: str):
    return search_teacher(id)

@app.delete("/teachers/{id}")
def remove_teacher(id: str):
    delete_teacher(id)
    return {"message": "Teacher deleted"}

@app.get("/classrooms/{classroom_number}")
def find_classroom(classroom_number: str):
    return search_classroom(classroom_number)

@app.delete("/classrooms/{classroom_number}")
def remove_classroom(classroom_number: str):
    delete_classroom(classroom_number)
    return {"message": "Classroom deleted"}

@app.get("/timetable/{id}")
def find_timetable(id: int):
    return search_timetable(id)

@app.delete("/timetable/{id}")
def remove_timetable(id: int):
    delete_timetable(id)
    return {"message": "Timetable entry deleted"}