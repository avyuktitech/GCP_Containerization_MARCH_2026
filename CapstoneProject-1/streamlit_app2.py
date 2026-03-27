import streamlit as st
import random
import time

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="E-Commerce Enterprise",
    page_icon="🛒",
    layout="wide"
)

# -----------------------------
# PREMIUM DESIGN SYSTEM
# -----------------------------
st.markdown("""
<style>

/* GLOBAL BACKGROUND */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
}

/* NAVBAR */
.navbar {
    background: #0f172a;
    padding: 14px;
    border-radius: 8px;
    color: #ffffff;
    font-size: 22px;
    font-weight: 600;
    text-align: center;
}

/* HERO */
.hero {
    background: linear-gradient(to right, #2563eb, #38bdf8);
    padding: 25px;
    border-radius: 12px;
    color: white;
    text-align: center;
    margin-top: 10px;
}

/* SECTION TITLE */
.section-title {
    color: #1e293b;
    font-weight: 700;
    font-size: 22px;
    margin-bottom: 10px;
}

/* CARD */
.card {
    background: white;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.1);
    transition: 0.25s;
}
.card:hover {
    transform: translateY(-5px);
}

/* PRODUCT NAME */
.product-name {
    color: #0f172a;
    font-size: 18px;
    font-weight: 600;
}

/* PRICE */
.price {
    color: #2563eb;
    font-size: 20px;
    font-weight: bold;
}

/* BUTTON */
.stButton>button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    padding: 8px 14px;
    border: none;
}
.stButton>button:hover {
    background-color: #1d4ed8;
}

/* PANEL */
.panel {
    background: white;
    padding: 16px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
}

/* TEXT */
p, label {
    color: #334155;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# DATA
# -----------------------------
products = [
    {"id": 1, "name": "Laptop", "price": 80000, "category": "Electronics",
     "img": "https://cdn-icons-png.flaticon.com/512/2920/2920277.png"},
    {"id": 2, "name": "Smartphone", "price": 30000, "category": "Electronics",
     "img": "https://cdn-icons-png.flaticon.com/512/15/15874.png"},
    {"id": 3, "name": "Headphones", "price": 2000, "category": "Accessories",
     "img": "https://cdn-icons-png.flaticon.com/512/727/727245.png"},
    {"id": 4, "name": "Shoes", "price": 2500, "category": "Fashion",
     "img": "https://cdn-icons-png.flaticon.com/512/892/892458.png"},
    {"id": 5, "name": "Watch", "price": 5000, "category": "Fashion",
     "img": "https://cdn-icons-png.flaticon.com/512/747/747310.png"},
    {"id": 6, "name": "Backpack", "price": 1500, "category": "Travel",
     "img": "https://cdn-icons-png.flaticon.com/512/1046/1046857.png"}
]

if "cart" not in st.session_state:
    st.session_state.cart = []

# -----------------------------
# NAVBAR
# -----------------------------
st.markdown('<div class="navbar">🛒 Enterprise E-Commerce Platform</div>', unsafe_allow_html=True)

# -----------------------------
# HERO
# -----------------------------
st.markdown("""
<div class="hero">
<h2>Scale-Ready Modern Commerce</h2>
<p>Microservices | Kubernetes | CI/CD | Observability</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# KPI
# -----------------------------
c1, c2, c3 = st.columns(3)
c1.metric("Total Products", len(products))
c2.metric("Cart Items", len(st.session_state.cart))
c3.metric("Cart Value", f"₹{sum(p['price'] for p in st.session_state.cart)}")

# -----------------------------
# LAYOUT
# -----------------------------
left, center, right = st.columns([1, 3, 1])

# LEFT PANEL
with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Filters</div>', unsafe_allow_html=True)

    category = st.selectbox(
        "Category",
        ["All"] + list(set(p["category"] for p in products))
    )

    price = st.slider("Price Range", 0, 100000, (0, 100000))
    st.markdown('</div>', unsafe_allow_html=True)

# FILTER
filtered = [
    p for p in products
    if (category == "All" or p["category"] == category)
    and price[0] <= p["price"] <= price[1]
]

# CENTER PRODUCTS
with center:
    st.markdown('<div class="section-title">Products</div>', unsafe_allow_html=True)

    cols = st.columns(3)

    for i, p in enumerate(filtered):
        with cols[i % 3]:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.image(p["img"], width=110)
            st.markdown(f'<div class="product-name">{p["name"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="price">₹{p["price"]}</div>', unsafe_allow_html=True)

            if st.button("Add to Cart", key=p["id"]):
                st.session_state.cart.append(p)
                st.toast("Added to cart")

            st.markdown('</div>', unsafe_allow_html=True)

# RIGHT PANEL
with right:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Cart</div>', unsafe_allow_html=True)

    total = 0
    for item in st.session_state.cart:
        st.write(f"{item['name']} - ₹{item['price']}")
        total += item["price"]

    st.markdown("---")
    st.markdown(f"**Total: ₹{total}**")

    if st.button("Clear Cart"):
        st.session_state.cart = []

    if st.button("Checkout"):
        if not st.session_state.cart:
            st.warning("Cart is empty")
        else:
            with st.spinner("Processing..."):
                time.sleep(2)

            if random.random() < 0.3:
                st.error("Payment Failed")
            else:
                st.success("Order Successful")
                st.session_state.cart = []

    st.markdown('</div>', unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown("© 2026 Enterprise HCL GKE - Commerce Platform | DevOps Ready")
