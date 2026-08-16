import streamlit as st
from utils.data import DARK_STORE, CATEGORIES, PRODUCTS
from utils.cart import init_state, cart_item_count

st.set_page_config(page_title="QuickCart", page_icon="🛒", layout="wide")
init_state()

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
