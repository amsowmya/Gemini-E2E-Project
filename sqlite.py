import sqlite3

connection = sqlite3.connect("student.db")

# create a cursor object to insert record, create table
cursor = connection.cursor()

# create the table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), 
SECTION VARCHAR(25));
"""

cursor.execute(table_info)

# insert some more record 
cursor.execute('''Insert into STUDENT values('Sam', 'Data Scientist', 'A')''')
cursor.execute('''Insert into STUDENT values('San', 'Data', 'B')''')
cursor.execute('''Insert into STUDENT values('Kumar', 'Devops', 'A')''')
cursor.execute('''Insert into STUDENT values('Pujar', 'Devops', 'A')''')
cursor.execute('''Insert into STUDENT values('Gabber', 'Data Scientist', 'A')''')

# display all the records
print("The inserted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# commit your changes in the database
connection.commit()
connection.close()