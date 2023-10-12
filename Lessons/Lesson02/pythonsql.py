import sqlite3

# first thing we do is connect to the database
connection = sqlite3.connect('C:\Program Files\SqLiteStudio\ckcsdb')
print(connection.total_changes)

# reading data from the database
cursor = connection.cursor()
rows = cursor.execute('SELECT * FROM employees')

for row in rows:
    print(row)

# update command
new_salary = 2400000
emp_id = 100
cursor.execute('UPDATE employees SET salary = ? WHERE employee_id = ?', (new_salary, emp_id))

print(connection.total_changes)
connection.commit()

