import streamlit as st
from utils.data import PRODUCTS, CATEGORIES
from utils.cart import init_state, add_to_cart, cart_item_count
from utils.auth import require_login, render_account_sidebar

st.set_page_config(page_title="Browse Products | QuickCart", page_icon="🛍️", layout="wide")
require_login()
render_account_sidebar()
init_state()

st.title("🛍️ Browse Products")
st.caption(f"🛒 {cart_item_count()} items in cart")

# ---- Filters ----
col_search, col_cat = st.columns([2, 1])
with col_search:
    search_term = st.text_input("Search products", placeholder="e.g. milk, chips, juice")
with col_cat:
    selected_category = st.selectbox("Category", ["All"] + CATEGORIES)

filtered = PRODUCTS
if selected_category != "All":
    filtered = [p for p in filtered if p["category"] == selected_category]
if search_term:
    filtered = [p for p in filtered if search_term.lower() in p["name"].lower()]

st.divider()

if not filtered:
    st.warning("No products match your filters.")
else:
    # Group by category for a cleaner layout
    grouped = {}
    for p in filtered:
        grouped.setdefault(p["category"], []).append(p)

    for category, items in grouped.items():
        st.markdown(f"### {category}")
        cols = st.columns(4)
        for i, product in enumerate(items):
            with cols[i % 4]:
                with st.container(border=True):
                    st.markdown(
                        f"<div style='font-size:44px; text-align:center'>{product['emoji']}</div>",
                        unsafe_allow_html=True,
                    )
                    st.markdown(f"**{product['name']}**")
                    st.caption(f"{product['unit']} · ETA {product['eta']}")
                    st.write(f"₹{product['price']}")
                    qty = st.number_input(
                        "Qty", min_value=1, max_value=10, value=1,
                        key=f"qty_{product['id']}", label_visibility="collapsed",
                    )
                    if st.button("Add to cart", key=f"add_{product['id']}", use_container_width=True):
                        add_to_cart(product["id"], qty)
                        st.toast(f"Added {qty} × {product['name']} to cart", icon="✅")
        st.divider()
