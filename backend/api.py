from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os

from models.student_db import add_student, get_students, delete_student, search_student, update_student
from models.teacher_db import add_teacher, get_teachers, delete_teacher, search_teacher, update_teacher
from models.classroom_db import add_classroom, get_classrooms, delete_classroom, search_classroom, update_classroom
from models.timetable_db import add_timetable, get_timetable, delete_timetable, search_timetable, update_timetable

app = FastAPI()
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

@app.get("/")
def root():
    return RedirectResponse(url="/static/login.html")

@app.post("/login")
def login(username: str, password: str):
    if username == os.getenv("ADMIN_USERNAME") and password == os.getenv("ADMIN_PASSWORD"):
        return {"message": "Login successful"}
    return {"message": "Invalid credentials"}

# ---------- STUDENTS ----------

@app.get("/students")
def read_students():
    return get_students()

@app.post("/students")
def create_student(roll_no: str, name: str, age: int, gender: str, section: str, gmail: str, major_subject: str):
    add_student(roll_no, name, age, gender, section, gmail, major_subject)
    return {"message": "Student added"}

@app.get("/students/{roll_no}")
def find_student(roll_no: str):
    return search_student(roll_no)

@app.put("/students/{roll_no}")
def edit_student(roll_no: str, name: str, age: int, gender: str, section: str, gmail: str, major_subject: str):
    update_student(roll_no, name, age, gender, section, gmail, major_subject)
    return {"message": "Student updated"}

@app.delete("/students/{roll_no}")
def remove_student(roll_no: str):
    delete_student(roll_no)
    return {"message": "Student deleted"}

# ---------- TEACHERS ----------

@app.get("/teachers")
def read_teachers():
    return get_teachers()

@app.post("/teachers")
def create_teacher(id: str, name: str, gender: str, subject: str, specialization: str):
    add_teacher(id, name, gender, subject, specialization)
    return {"message": "Teacher added"}

@app.get("/teachers/{id}")
def find_teacher(id: str):
    return search_teacher(id)

@app.put("/teachers/{id}")
def edit_teacher(id: str, name: str, gender: str, subject: str, specialization: str):
    update_teacher(id, name, gender, subject, specialization)
    return {"message": "Teacher updated"}

@app.delete("/teachers/{id}")
def remove_teacher(id: str):
    delete_teacher(id)
    return {"message": "Teacher deleted"}

# ---------- CLASSROOMS ----------

@app.get("/classrooms")
def read_classrooms():
    return get_classrooms()

@app.post("/classrooms")
def create_classroom(classroom_number: str, capacity: int, department: str, section: str):
    add_classroom(classroom_number, capacity, department, section)
    return {"message": "Classroom added"}

@app.get("/classrooms/{classroom_number}")
def find_classroom(classroom_number: str):
    return search_classroom(classroom_number)

@app.put("/classrooms/{classroom_number}")
def edit_classroom(classroom_number: str, capacity: int, department: str, section: str):
    update_classroom(classroom_number, capacity, department, section)
    return {"message": "Classroom updated"}

@app.delete("/classrooms/{classroom_number}")
def remove_classroom(classroom_number: str):
    delete_classroom(classroom_number)
    return {"message": "Classroom deleted"}

# ---------- TIMETABLE ----------

@app.get("/timetable")
def read_timetable():
    return get_timetable()

@app.post("/timetable")
def create_timetable(day: str, time: str, classroom_number: str, section: str, assigned_class: str, assigned_teacher: str):
    add_timetable(day, time, classroom_number, section, assigned_class, assigned_teacher)
    return {"message": "Timetable entry added"}

@app.get("/timetable/{id}")
def find_timetable(id: int):
    return search_timetable(id)

@app.put("/timetable/{id}")
def edit_timetable(id: int, day: str, time: str, classroom_number: str, section: str, assigned_class: str, assigned_teacher: str):
    update_timetable(id, day, time, classroom_number, section, assigned_class, assigned_teacher)
    return {"message": "Timetable entry updated"}

@app.delete("/timetable/{id}")
def remove_timetable(id: int):
    delete_timetable(id)
    return {"message": "Timetable entry deleted"}