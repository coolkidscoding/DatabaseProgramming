import sqlite3

connection = sqlite3.connect('C:\\Program Files\\SQLiteStudio\\ckcsdb')

print(connection.total_changes)

cursor = connection.cursor()
rows = cursor.execute("SELECT * FROM employees;")

for row in rows:
    print(row)
    
target_job_id = 9
rows = cursor.execute("SELECT * FROM employees WHERE job_id = ?;", (target_job_id,))

for row in rows:
    print(row)
    
from contextlib import closing

with closing(sqlite3.connect('C:\\Program Files\\SQLiteStudio\\ckcsdb')) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT * FROM employees;")
        for row in rows:
            print(row)
