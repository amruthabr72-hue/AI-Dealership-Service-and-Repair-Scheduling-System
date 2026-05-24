import sqlite3
import pandas as pd

# Save appointment
def save_appointment(data):

    conn = sqlite3.connect('dealership.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO appointments
    (
    customer_name,
    phone,
    vehicle_model,
    service_type,
    issue_description,
    appointment_date,
    appointment_time,
    status
    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)

    conn.commit()
    conn.close()

# Get appointments
def get_appointments():

    conn = sqlite3.connect('dealership.db')

    df = pd.read_sql_query(
        "SELECT * FROM appointments",
        conn
    )

    conn.close()

    return df
def check_slot(date, time):
    
    conn = sqlite3.connect('dealership.db')

    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM appointments
    WHERE appointment_date=? AND appointment_time=?
    ''', (date, time))

    result = cursor.fetchone()

    conn.close()

    return result