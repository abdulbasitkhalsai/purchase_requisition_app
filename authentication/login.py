import streamlit as st
from datetime import datetime, timedelta


SESSION_DURATION = timedelta(hours=2)

# Dummy credentials
USERS = {
    "admin": {"password": "admin123",
              "email": "admin@gmail.com",
              "userName": "Admin",
              "dept": "Admin",
              "division": "Admin",
              "location": "Head Office",
              "region": "Karachi",
              },
    "user": {
        "password": "user123",
        "userid": "2",
        "username": "Regular User",
        "dept": "Finance",
        "division": "Accounts",
        "empcode": "EMP002",
        "location": "Branch A",
        "region": "North"
    }
}

def login_ui():
    st.subheader("🔐 Login Required")
    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.form_submit_button("Login")

        if login_btn:
            if username in USERS and USERS[username]["password"] == password:
            # if username in USERS and USERS.get(username, {}).get("password"):
                st.session_state.authenticated = True
                st.session_state.login_time = datetime.now()
                for key, value in USERS[username].items():
                    if key != "password":
                        st.session_state[key] = value
                st.rerun()
            else:
                st.error("Invalid credentials.")

# def is_authenticated():
#     return st.session_state.get("authenticated", False)
def is_authenticated():
    login_time = st.session_state.get("login_time", None)
    if st.session_state.get("authenticated", False) and login_time:
        if datetime.now() - login_time < SESSION_DURATION:
            return True
        else:
            # Expired
            st.session_state.authenticated = False
            st.warning("Session expired. Please log in again.")
            return False
    return False
