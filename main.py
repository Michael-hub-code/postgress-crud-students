"""
Simple PostgreSQL CRUD for the 'students' table.

Functions required by the assignment:
- getAllStudents()
- addStudent(first_name, last_name, email, enrollment_date)
- updateStudentEmail(student_id, new_email)
- deleteStudent(student_id)
"""

import os
import sys
import psycopg2
from psycopg2.extras import RealDictCursor

def get_conn():
    """
    Opens connection to PostgreSQL database using environment variables.
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("PGHOST", "localhost"),
            port=os.getenv("PGPORT", "5432"),
            dbname=os.getenv("PGDATABASE", "postgres"),
            user=os.getenv("PGUSER", "postgres"),
            password=os.getenv("PGPASSWORD", "")
        )
        return conn
    except Exception as e:
        print(f"[ERROR] Database connection failed: {e}")
        sys.exit(1)

def getAllStudents():
    """
    Retrieves and prints all students.
    """
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM students ORDER BY student_id;")
            rows = cur.fetchall()
            print("\n=== Students ===")
            for r in rows:
                print(f"{r['student_id']}: {r['first_name']} {r['last_name']} | {r['email']} | {r['enrollment_date']}")
            print("================\n")
    except Exception as e:
        print(f"[ERROR] getAllStudents: {e}")
    finally:
        conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    """
    Inserts a new student.
    """
    conn = get_conn()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("""
                INSERT INTO students (first_name, last_name, email, enrollment_date)
                VALUES (%s, %s, %s, %s);
            """, (first_name, last_name, email, enrollment_date))
            print("[OK] Student added successfully.")
    except Exception as e:
        conn.rollback()
        print(f"[ERROR] addStudent: {e}")
    finally:
        conn.close()

def updateStudentEmail(student_id, new_email):
    """
    Updates a student's email by ID.
    """
    conn = get_conn()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id))
            if cur.rowcount == 0:
                print("[WARN] No student with that ID.")
            else:
                print("[OK] Email updated successfully.")
    except Exception as e:
        conn.rollback()
        print(f"[ERROR] updateStudentEmail: {e}")
    finally:
        conn.close()

def deleteStudent(student_id):
    """
    Deletes a student by ID.
    """
    conn = get_conn()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
            if cur.rowcount == 0:
                print("[WARN] No student with that ID.")
            else:
                print("[OK] Student deleted successfully.")
    except Exception as e:
        conn.rollback()
        print(f"[ERROR] deleteStudent: {e}")
    finally:
        conn.close()

def menu():
    while True:
        print("""
Choose an action:
1. View all students
2. Add a student
3. Update student email
4. Delete a student
0. Exit
""")
        choice = input("Enter choice: ")

        if choice == "1":
            getAllStudents()
        elif choice == "2":
            first = input("First name: ")
            last = input("Last name: ")
            email = input("Email: ")
            date = input("Enrollment date (YYYY-MM-DD): ")
            addStudent(first, last, email, date)
        elif choice == "3":
            sid = input("Student ID: ")
            new_email = input("New email: ")
            updateStudentEmail(sid, new_email)
        elif choice == "4":
            sid = input("Student ID to delete: ")
            deleteStudent(sid)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nProgram terminated.")
