import streamlit as st
import sqlite3
import pandas as pd

st.title("📊 Admin Dashboard")

conn = sqlite3.connect('dealership.db')

df = pd.read_sql_query(
    "SELECT * FROM appointments",
    conn
)

# Show appointments table
st.dataframe(df)

# Analytics section
st.subheader("Service Analytics")

service_counts = df['service_type'].value_counts()

st.bar_chart(service_counts)

appointment_id = st.number_input(
    "Enter Appointment ID",
    min_value=1
)

new_status = st.selectbox(
    "Update Status",
    [
        "Pending",
        "Confirmed",
        "In Progress",
        "Completed"
    ]
)

if st.button("Update Status"):

    cursor = conn.cursor()

    cursor.execute('''
    UPDATE appointments
    SET status=?
    WHERE id=?
    ''',
    (new_status, appointment_id))

    conn.commit()

    st.success("Status Updated!")

conn.close()