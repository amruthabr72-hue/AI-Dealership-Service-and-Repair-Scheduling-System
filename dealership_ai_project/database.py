import sqlite3

conn = sqlite3.connect('dealership.db')
cursor = conn.cursor()

# Appointments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    phone TEXT,
    vehicle_model TEXT,
    service_type TEXT,
    issue_description TEXT,
    appointment_date TEXT,
    appointment_time TEXT,
    status TEXT
)
''')

# Admin table
cursor.execute('''
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
''')

conn.commit()
conn.close()

print("Database created successfully")