"""Session-state helpers for the cart. Pure frontend state — resets each session."""

import streamlit as st


def init_state():
    if "cart" not in st.session_state:
        st.session_state.cart = {}  # {product_id: quantity}
    if "orders" not in st.session_state:
        st.session_state.orders = []  # list of past order dicts


def add_to_cart(product_id, qty=1):
    st.session_state.cart[product_id] = st.session_state.cart.get(product_id, 0) + qty


def set_quantity(product_id, qty):
    if qty <= 0:
        st.session_state.cart.pop(product_id, None)
    else:
        st.session_state.cart[product_id] = qty


def remove_from_cart(product_id):
    st.session_state.cart.pop(product_id, None)


def clear_cart():
    st.session_state.cart = {}


def cart_item_count():
    return sum(st.session_state.cart.values())


def cart_total(products_by_id):
    total = 0
    for pid, qty in st.session_state.cart.items():
        product = products_by_id.get(pid)
        if product:
            total += product["price"] * qty
    return total
