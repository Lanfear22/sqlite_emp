import sqlite3


conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute("""DROP TABLE Employees""")

c.execute("""CREATE TABLE Employees (
     employee_id INTEGER PRIMARY KEY,    
     first_name text,
     last_name text,
     current_contract text
     )""")

c.execute("INSERT INTO Employees VALUES ('John', 'Smith', 'OVHD')")

c.execute("INSERT INTO Employees VALUES ('Jane', 'Smith', 'OVHD')")

conn.commit()

c.execute("SELECT * FROM Employees WHERE last_name='Smith'")

print(c.fetchall())

conn.commit()

conn.close()







