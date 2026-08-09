from db import get_connection

def add_classroom(classroom_number, capacity, department):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO classrooms VALUES (%s, %s, %s)",
        (classroom_number, capacity, department)
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