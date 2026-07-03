import sqlite3
import os

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE STUDENT(
    NAME TEXT,
    CLASS TEXT,
    SECTION TEXT,
    MARKS INTEGER
)
""")

students = [
    ("Subbu", "DataScience", "B", 70),
    ("Krish", "ML", "A", 90),
    ("Tarak", "AI", "B", 65),
    ("Ram", "DataAnalyst", "A", 70),
    ("Somu", "DataScience", "B", 80)
]

cursor.executemany(
    "INSERT INTO STUDENT VALUES (?, ?, ?, ?)",
    students
)

connection.commit()

print(cursor.execute("SELECT * FROM STUDENT").fetchall())

connection.close()