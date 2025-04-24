import streamlit as st
from authentication.login import is_authenticated, login_ui

def render_sidebar():
    with st.sidebar:
        if not is_authenticated():
            login_ui()
        else:
            col1, col2 = st.columns([1, 4])
            with col1:
                st.image("https://i.pinimg.com/736x/8b/16/7a/8b167af653c2399dd93b952a48740620.jpg", width=50, use_container_width=False)
            with col2:
                st.markdown(
                    f"<p style='margin-top: 15px;'>Hey, <b>{st.session_state.get('username', 'User')}</b></p>",
                    unsafe_allow_html=True
                )
                # st.markdown(f"Hey, {st.session_state.get('username', 'User')}!")
            if st.button("🚪 Logout"):
                st.session_state.authenticated = False
                st.rerun()
