from db import get_connection

def add_teacher(id, name, gender, subject, specialization):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO teachers VALUES (%s, %s, %s, %s, %s)",
        (id, name, gender, subject, specialization)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_teachers():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM teachers")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def delete_teacher(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM teachers WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()

def search_teacher(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM teachers WHERE id = %s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row