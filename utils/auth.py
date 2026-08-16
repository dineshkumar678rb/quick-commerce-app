"""Demo authentication for the frontend-only QuickCart app.
No backend/database — credentials are hardcoded for demo purposes only.
Do NOT use this approach for a real production app.
"""

import streamlit as st

DEMO_USERS = {
    "demo": "demo123",
    "dinesh": "quickcart123",
}


def init_auth_state():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = None


def attempt_login(username, password):
    if username in DEMO_USERS and DEMO_USERS[username] == password:
        st.session_state.authenticated = True
        st.session_state.username = username
        return True
    return False


def login_as_guest():
    st.session_state.authenticated = True
    st.session_state.username = "Guest"


def logout():
    st.session_state.authenticated = False
    st.session_state.username = None


def require_login():
    """Call at the very top of any protected page.
    Stops rendering and shows a message if the user isn't logged in."""
    init_auth_state()
    if not st.session_state.authenticated:
        st.warning("Please log in to access this page.", icon="🔒")
        st.page_link("Home.py", label="Go to Login", icon="🏠")
        st.stop()


def render_account_sidebar():
    """Shows who's logged in + a logout button. Call on protected pages."""
    with st.sidebar:
        st.markdown(f"👤 Logged in as **{st.session_state.username}**")
        if st.button("Log out", use_container_width=True):
            logout()
            st.rerun()
