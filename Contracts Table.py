import sqlite3

conn = sqlite3.connect('employee.db')

c=conn.cursor()

c.execute("""CREATE TABLE Contracts (
     CONTRACT_ID INTEGER PRIMARY KEY,
     CONTRACT_NAME STR,
     YEAR_ENDING STR,
     NUM_EMPLOYEES INTEGER,
     LIST_EMPLOYEES BLOB,
     CONTRACT_OVERVIEW BLOB
     )""")
