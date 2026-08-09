from db import get_connection

def add_classroom(classroom_number, capacity, department, section):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO classrooms VALUES (%s, %s, %s, %s)",
        (classroom_number, capacity, department, section)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_classrooms():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM classrooms")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def delete_classroom(classroom_number):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM classrooms WHERE classroom_number = %s", (classroom_number,))
    conn.commit()
    cur.close()
    conn.close()

def search_classroom(classroom_number):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM classrooms WHERE classroom_number = %s", (classroom_number,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def update_classroom(classroom_number, capacity, department, section):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE classrooms SET capacity=%s, department=%s, section=%s WHERE classroom_number=%s",
        (capacity, department, section, classroom_number)
    )
    conn.commit()
    cur.close()
    conn.close()