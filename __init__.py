import sqlite3


conn = sqlite3.connect('employee.db')

# Creating the Cursor
c = conn.cursor()

# Delete tables to be recreated each time the program runs
c.execute("""DROP TABLE Employees""")

c.execute("""DROP TABLE Contracts""")

# Create 'Employees' Table
c.execute("""CREATE TABLE Employees (
     EMPLOYEE_ID INTEGER PRIMARY KEY,    
     FIRST_NAME STR,
     LAST_NAME STR,
     CURRENT_CONTRACT STR
     )""")

# Create 'Contracts' Table
c.execute("""CREATE TABLE Contracts (
     CONTRACT_ID INTEGER PRIMARY KEY,
     CONTRACT_NAME STR,
     YEAR_ENDING STR,
     NUM_EMPLOYEES INTEGER,
     LIST_EMPLOYEES BLOB,
     CONTRACT_OVERVIEW BLOB
     )""")

# Insert Test Data into Tables
c.execute("""INSERT INTO Employees (FIRST_NAME, LAST_NAME, CURRENT_CONTRACT) 
     VALUES ('John', 'Smith', 'OVHD')""")

c.execute("""INSERT INTO Employees (FIRST_NAME, LAST_NAME, CURRENT_CONTRACT) 
     VALUES ('Jane', 'Smith', 'OVHD')""")

c.execute("""INSERT INTO Contracts (CONTRACT_NAME, YEAR_ENDING, NUM_EMPLOYEES, LIST_EMPLOYEES, CONTRACT_OVERVIEW) 
     VALUES ('SCOOBYSNACKS', '2019', '10', 'Chris Howell, Dave Parsram, Joe Ferner, Ed Degeyter', 'Focuses on CNO tools development primarily using C, C++, Java, and Python.  Follow on to GRIFFIN.')""")

# Commit table creation and data insertion
conn.commit()

# Select and Print Employees inserted that have the last name 'Smith', to see output
c.execute("SELECT * FROM Employees WHERE LAST_NAME='Smith'")

print(c.fetchall())

c.execute("SELECT * FROM Contracts")

print(c.fetchall())

conn.commit()

conn.close()







