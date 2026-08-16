import streamlit as st
from utils.cart import init_state

st.set_page_config(page_title="Orders | QuickCart", page_icon="📦", layout="wide")
init_state()

st.title("📦 Your Orders")

orders = st.session_state.orders

if not orders:
    st.info("No orders placed yet in this session.", icon="🧾")
else:
    for order in orders:
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**Order #{order['id']}**  ·  {order['placed_at']}")
                st.caption(f"{order['store']} · Delivered in {order['eta']}")
            with col2:
                st.markdown(f"### ₹{order['total']}")

            for item in order["items"]:
                st.write(f"- {item['name']} × {item['qty']} — ₹{item['price'] * item['qty']}")
