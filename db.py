import sqlite3

def get_connection():
    return sqlite3.connect("students.db")

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        campus TEXT,
        module TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_student(name, email, campus, module):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO students (name, email, campus, module) VALUES (?, ?, ?, ?)", 
                    (name, email, campus, module))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False # Email already exists
    finally:
        conn.close()

def get_all_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, campus, module FROM students")
    data = cur.fetchall()
    conn.close()
    return data

def get_student_by_id(s_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id = ?", (s_id,))
    student = cur.fetchone()
    conn.close()
    return student

def update_student(s_id, name, email, campus, module):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE students SET name=?, email=?, campus=?, module=? WHERE id=?", 
                (name, email, campus, module, s_id))
    conn.commit()
    conn.close()

def delete_student(s_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", (s_id,))
    conn.commit()
    conn.close()