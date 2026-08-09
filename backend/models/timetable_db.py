from db import get_connection

def add_timetable(day, time, classroom_number, section, assigned_class, assigned_teacher):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO timetable (day, time, classroom_number, section, assigned_class, assigned_teacher) VALUES (%s, %s, %s, %s, %s, %s)",
        (day, time, classroom_number, section, assigned_class, assigned_teacher)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_timetable():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, day, time, classroom_number, section, assigned_class, assigned_teacher FROM timetable")
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
    cur.execute("SELECT id, day, time, classroom_number, section, assigned_class, assigned_teacher FROM timetable WHERE id = %s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def update_timetable(id, day, time, classroom_number, section, assigned_class, assigned_teacher):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE timetable SET day=%s, time=%s, classroom_number=%s, section=%s, assigned_class=%s, assigned_teacher=%s WHERE id=%s",
        (day, time, classroom_number, section, assigned_class, assigned_teacher, id)
    )
    conn.commit()
    cur.close()
    conn.close()