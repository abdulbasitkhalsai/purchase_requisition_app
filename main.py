import streamlit as st
from authentication.login import login_ui, is_authenticated
from form.requisition_form import requisition_form
from components.sidebar import render_sidebar

st.set_page_config(page_title="Purchase Requisition", layout="wide")

# Sidebar
render_sidebar()

# Login and form rendering
if is_authenticated():
    requisition_form()
