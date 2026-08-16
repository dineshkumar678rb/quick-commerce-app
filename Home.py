import streamlit as st
from utils.data import DARK_STORE, CATEGORIES, PRODUCTS
from utils.cart import init_state, cart_item_count
from utils.auth import init_auth_state, attempt_login, login_as_guest, render_account_sidebar

st.set_page_config(page_title="QuickCart", page_icon="🛒", layout="wide")
init_state()
init_auth_state()

# ---- Login gate ----
if not st.session_state.authenticated:
    st.title("🛒 QuickCart")
    st.caption("Log in to start shopping")

    tab_login, tab_guest = st.tabs(["Login", "Quick Guest Access"])

    with tab_login:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Log in", type="primary", use_container_width=True)
            if submitted:
                if attempt_login(username, password):
                    st.success(f"Welcome, {username}!")
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
        st.caption("Demo credentials: `demo` / `demo123`")

    with tab_guest:
        st.write("No account needed — jump straight into the demo.")
        if st.button("Continue as Guest", use_container_width=True):
            login_as_guest()
            st.rerun()

    st.stop()

# ---- Logged-in sidebar ----
render_account_sidebar()

# ---- Header ----
col1, col2 = st.columns([4, 1])
with col1:
    st.title("🛒 QuickCart")
    st.caption(f"Delivering in {DARK_STORE['delivery_promise']} from {DARK_STORE['name']}")
with col2:
    st.metric("Items in cart", cart_item_count())

st.divider()

# ---- Hero ----
st.subheader("Groceries delivered in minutes, not hours.")
st.write(
    "Browse fresh produce, dairy, snacks, beverages, and personal care items — "
    "all picked from your nearest dark store."
)

# ---- Category shortcuts ----
st.markdown("### Shop by category")
cols = st.columns(len(CATEGORIES))
category_icons = {
    "Fruits & Vegetables": "🥦",
    "Dairy & Bread": "🥛",
    "Snacks": "🍪",
    "Beverages": "🥤",
    "Personal Care": "🧴",
}
for col, cat in zip(cols, CATEGORIES):
    with col:
        st.markdown(f"<div style='text-align:center; font-size:40px'>{category_icons[cat]}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align:center'>{cat}</div>", unsafe_allow_html=True)

st.divider()

# ---- Trending products preview ----
st.markdown("### Trending right now")
preview = PRODUCTS[:4]
cols = st.columns(4)
for col, product in zip(cols, preview):
    with col:
        with st.container(border=True):
            st.markdown(f"<div style='font-size:36px; text-align:center'>{product['emoji']}</div>", unsafe_allow_html=True)
            st.markdown(f"**{product['name']}**")
            st.caption(product["unit"])
            st.write(f"₹{product['price']}")

st.divider()
st.info("Use the sidebar to go to **Browse Products**, view your **Cart**, or check **Orders**.", icon="👈")
