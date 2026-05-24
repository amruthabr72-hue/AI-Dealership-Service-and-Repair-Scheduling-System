import streamlit as st
from utils import save_appointment, check_slot
from issue_classifier import predict_issue

st.title("📅 Book Appointment")

customer_name = st.text_input("Customer Name")

phone = st.text_input("Phone Number")

vehicle_model = st.text_input("Vehicle Model")

service_type = st.selectbox(
    "Service Type",
    [
        "Oil Change",
        "Brake Repair",
        "Battery Service",
        "General Service"
    ]
)

issue_description = st.text_area(
    "Describe Vehicle Issue"
)
if issue_description:
    
    predicted_issue = predict_issue(issue_description)

    st.info(f"Predicted Issue: {predicted_issue}")

appointment_date = st.date_input(
    "Appointment Date"
)

appointment_time = st.time_input(
    "Appointment Time"
)
service_costs = {
    "Oil Change": 1500,
    "Brake Repair": 4000,
    "Battery Service": 3000,
    "General Service": 2500
}

estimated_cost = service_costs[service_type]

st.write(f"Estimated Service Cost: ₹{estimated_cost}")

if st.button("Book Appointment"):
    
    slot = check_slot(
        str(appointment_date),
        str(appointment_time)
    )

    if slot:

        st.error("Selected slot already booked!")

    else:

        data = (
            customer_name,
            phone,
            vehicle_model,
            service_type,
            issue_description,
            str(appointment_date),
            str(appointment_time),
            "Pending"
        )

        save_appointment(data)

        st.success("Appointment booked successfully!")