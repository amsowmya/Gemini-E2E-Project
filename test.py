import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM STUDENT")
data = cursor.fetchall()
print(data)
for row in data:
    print(row)