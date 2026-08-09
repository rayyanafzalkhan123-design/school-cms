from db import get_connection

def add_timetable(day, time, classroom_number, assigned_teacher, assigned_class):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO timetable (day, time, classroom_number, assigned_teacher, assigned_class) VALUES (%s, %s, %s, %s, %s)",
        (day, time, classroom_number, assigned_teacher, assigned_class)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_timetable():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM timetable")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def delete_timetable(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM timetable WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()

def search_timetable(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM timetable WHERE id = %s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row