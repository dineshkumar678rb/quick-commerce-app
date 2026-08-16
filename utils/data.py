"""Static sample data for the Quick Commerce frontend demo.
No backend/database — everything lives in memory for this session.
"""

CATEGORIES = ["Fruits & Vegetables", "Dairy & Bread", "Snacks", "Beverages", "Personal Care"]

PRODUCTS = [
    {"id": 1, "name": "Fresh Bananas (6 pcs)", "category": "Fruits & Vegetables", "price": 45, "unit": "1 dozen", "emoji": "🍌", "eta": "10 mins"},
    {"id": 2, "name": "Tomatoes", "category": "Fruits & Vegetables", "price": 30, "unit": "500 g", "emoji": "🍅", "eta": "10 mins"},
    {"id": 3, "name": "Onions", "category": "Fruits & Vegetables", "price": 35, "unit": "1 kg", "emoji": "🧅", "eta": "12 mins"},
    {"id": 4, "name": "Toned Milk", "category": "Dairy & Bread", "price": 28, "unit": "500 ml", "emoji": "🥛", "eta": "8 mins"},
    {"id": 5, "name": "Brown Bread", "category": "Dairy & Bread", "price": 55, "unit": "400 g", "emoji": "🍞", "eta": "9 mins"},
    {"id": 6, "name": "Paneer", "category": "Dairy & Bread", "price": 90, "unit": "200 g", "emoji": "🧀", "eta": "10 mins"},
    {"id": 7, "name": "Potato Chips", "category": "Snacks", "price": 20, "unit": "52 g", "emoji": "🍟", "eta": "11 mins"},
    {"id": 8, "name": "Chocolate Cookies", "category": "Snacks", "price": 40, "unit": "200 g", "emoji": "🍪", "eta": "11 mins"},
    {"id": 9, "name": "Mixed Nuts", "category": "Snacks", "price": 150, "unit": "250 g", "emoji": "🥜", "eta": "13 mins"},
    {"id": 10, "name": "Cola", "category": "Beverages", "price": 40, "unit": "750 ml", "emoji": "🥤", "eta": "9 mins"},
    {"id": 11, "name": "Orange Juice", "category": "Beverages", "price": 65, "unit": "1 L", "emoji": "🧃", "eta": "10 mins"},
    {"id": 12, "name": "Instant Coffee", "category": "Beverages", "price": 120, "unit": "100 g", "emoji": "☕", "eta": "10 mins"},
    {"id": 13, "name": "Shampoo", "category": "Personal Care", "price": 180, "unit": "180 ml", "emoji": "🧴", "eta": "14 mins"},
    {"id": 14, "name": "Toothpaste", "category": "Personal Care", "price": 55, "unit": "100 g", "emoji": "🪥", "eta": "12 mins"},
    {"id": 15, "name": "Hand Sanitizer", "category": "Personal Care", "price": 75, "unit": "100 ml", "emoji": "🧼", "eta": "12 mins"},
]

DARK_STORE = {
    "name": "QuickCart Dark Store — Koramangala",
    "address": "5th Block, Koramangala, Bengaluru",
    "delivery_promise": "10-15 mins",
}


def get_product_by_id(product_id):
    for p in PRODUCTS:
        if p["id"] == product_id:
            return p
    return None
