# 🛒 QuickCart — Quick Commerce Frontend (Streamlit)

A frontend-only Streamlit demo of a quick-commerce (10-15 min delivery) shopping app.
Browse products by category, add items to a cart, place an order, and view order history —
all in-memory for the session, no backend or database required.

## Features
- **Home** — hero section, category shortcuts, trending products
- **Browse Products** — search + category filter, add-to-cart with quantity picker
- **Cart** — edit quantities, remove items, delivery fee logic, place order
- **Orders** — session-based order history

## Tech
- Python 3.9+
- [Streamlit](https://streamlit.io/) — no backend, all state kept in `st.session_state`

## Run locally
```bash
python -m venv venv
source venv/bin/activate      # venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run Home.py
```

## Project structure
```
quick-commerce-app/
├── Home.py                       # entry point
├── pages/
│   ├── 1_🛍️_Browse_Products.py
│   ├── 2_🛒_Cart.py
│   └── 3_📦_Orders.py
├── utils/
│   ├── data.py                   # sample product/store data
│   └── cart.py                   # session-state cart helpers
├── requirements.txt
└── README.md
```

## Deploy on Streamlit Community Cloud
1. Push this repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io), connect the repo.
3. Set the entry point to `Home.py` and deploy.

## Notes
This is a **frontend-only** prototype — cart and order data reset when the session ends.
A real version would persist products/orders in a database (e.g. SQLite/Postgres) and add
auth, payments, and live delivery tracking.
