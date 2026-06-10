import sqlite3

conn = sqlite3.connect("company.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    message TEXT
)
""")

conn.commit()
conn.close()

print("Leads table created successfully!")