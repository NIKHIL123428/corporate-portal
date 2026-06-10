import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS departments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    department TEXT,
    employees INTEGER
)
""")

cursor.execute("INSERT INTO departments(department, employees) VALUES ('IT', 40)")
cursor.execute("INSERT INTO departments(department, employees) VALUES ('HR', 20)")
cursor.execute("INSERT INTO departments(department, employees) VALUES ('Sales', 30)")

conn.commit()
conn.close()

print("Data Inserted Successfully")