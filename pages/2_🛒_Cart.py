import datetime
import streamlit as st
from utils.data import PRODUCTS, get_product_by_id, DARK_STORE
from utils.cart import init_state, set_quantity, remove_from_cart, clear_cart, cart_total

st.set_page_config(page_title="Cart | QuickCart", page_icon="🛒", layout="wide")
init_state()

st.title("🛒 Your Cart")

products_by_id = {p["id"]: p for p in PRODUCTS}
cart = st.session_state.cart

if not cart:
    st.info("Your cart is empty. Head to **Browse Products** to add items.", icon="🛍️")
else:
    for pid, qty in list(cart.items()):
        product = get_product_by_id(pid)
        if not product:
            continue
        col1, col2, col3, col4, col5 = st.columns([1, 3, 2, 2, 1])
        with col1:
            st.markdown(f"<div style='font-size:32px'>{product['emoji']}</div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"**{product['name']}**")
            st.caption(product["unit"])
        with col3:
            new_qty = st.number_input(
                "Qty", min_value=0, max_value=10, value=qty,
                key=f"cart_qty_{pid}", label_visibility="collapsed",
            )
            if new_qty != qty:
                set_quantity(pid, new_qty)
                st.rerun()
        with col4:
            st.write(f"₹{product['price'] * qty}")
        with col5:
            if st.button("✕", key=f"remove_{pid}"):
                remove_from_cart(pid)
                st.rerun()
    st.divider()

    total = cart_total(products_by_id)
    delivery_fee = 15 if total < 200 else 0
    grand_total = total + delivery_fee

    col_a, col_b = st.columns([2, 1])
    with col_b:
        st.markdown(f"**Subtotal:** ₹{total}")
        st.markdown(f"**Delivery fee:** ₹{delivery_fee}" + (" (free above ₹200)" if delivery_fee == 0 else ""))
        st.markdown(f"### Total: ₹{grand_total}")

        if st.button("Place Order", type="primary", use_container_width=True):
            order = {
                "id": len(st.session_state.orders) + 1,
                "items": [
                    {"name": products_by_id[pid]["name"], "qty": qty, "price": products_by_id[pid]["price"]}
                    for pid, qty in cart.items()
                ],
                "total": grand_total,
                "placed_at": datetime.datetime.now().strftime("%d %b %Y, %I:%M %p"),
                "store": DARK_STORE["name"],
                "eta": DARK_STORE["delivery_promise"],
            }
            st.session_state.orders.insert(0, order)
            clear_cart()
            st.success("Order placed! Check the Orders page for details.", icon="🎉")
            st.rerun()

    with col_a:
        if st.button("Clear Cart"):
            clear_cart()
            st.rerun()
