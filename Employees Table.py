import sqlite3

conn = sqlite3.connect('employee.db')

c=conn.cursor()

c.execute("""CREATE TABLE Employees (
     EMPLOYEE_ID INTEGER PRIMARY KEY,    
     FIRST_NAME STR,
     LAST_NAME STR,
     CURRENT_CONTRACT STR
     )""")


c.execute("""INSERT INTO Employees (FIRST_NAME, LAST_NAME, CURRENT_CONTRACT) 
     VALUES ('Jane', 'Smith', 'OVHD')""")


# Commit table creation and data insertion
conn.commit()

# Select and Print Employees inserted that have the last name 'Smith', to see output
c.execute("SELECT * FROM Employees WHERE LAST_NAME='Smith'")

print(c.fetchall())