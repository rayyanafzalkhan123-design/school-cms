from db import get_connection

def add_student(roll_no, name, age, gender, section, gmail, major_subject):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (roll_no, name, age, gender, section, gmail, major_subject)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def delete_student(roll_no):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE roll_no = %s", (roll_no,))
    conn.commit()
    cur.close()
    conn.close()

def search_student(roll_no):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row