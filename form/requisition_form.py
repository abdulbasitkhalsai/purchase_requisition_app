import streamlit as st
from datetime import date

def requisition_form():
    st.title("📄 Purchase Requisition Form")

    with st.form("purchase_form"):
        col1, col2 = st.columns(2)
        with col1:
            employee_name = st.text_input("Employee Name")
            employee_id = st.text_input("Employee ID")
            email = st.text_input("Email")
        with col2:
            phone_number = st.text_input("Phone Number")
            location = st.selectbox("Location", ["Head Office", "Branch Office"])
        department = st.selectbox("Department", ["Procurement", "Admin", "IT", "Finance"])
        item_name = st.text_input("Item Name")
        quantity = st.number_input("Quantity", min_value=1)
        needed_by = st.date_input("Required By", min_value=date.today())
        justification = st.text_area("Justification")
        submitted = st.form_submit_button("Submit Request")

        if submitted:
            st.success("Request submitted successfully!")
            # TODO: Save to DB or Google Sheet
