import streamlit as st
import requests

# API Endpoints
BASE_URL = "http://127.0.0.1:8000"

# Fetch data
revenue = requests.get(f"{BASE_URL}/analytics/revenue").json()["total_revenue"]
top_products = requests.get(f"{BASE_URL}/analytics/top-products").json()["top_products"]

# Dashboard
st.title("E-Commerce Analytics Dashboard")
st.metric("Total Revenue", f"₹{revenue}")

st.header("Top-Selling Products")
for product in top_products:
    st.write(f"Product ID: {product[0]}, Sales: {product[1]}")
