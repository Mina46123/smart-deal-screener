import streamlit as st
import pandas as pd

# Mocked Bayut-style listings (replace this with scraped data later)
data = [
    {"title": "1BR in JVC by Sobha", "price": 950000, "size_sqft": 710, "bedrooms": 1, "developer": "Sobha", "year_built": 2022, "ready": True, "roi": 7.4},
    {"title": "1BR in Arjan", "price": 880000, "size_sqft": 590, "bedrooms": 1, "developer": "Smaller Dev", "year_built": 2018, "ready": True, "roi": 7.1},
    {"title": "1BR by Emaar in Dubai Hills", "price": 990000, "size_sqft": 640, "bedrooms": 1, "developer": "Emaar", "year_built": 2021, "ready": True, "roi": 6.9},
    {"title": "1BR in Business Bay", "price": 1020000, "size_sqft": 720, "bedrooms": 1, "developer": "Emaar", "year_built": 2020, "ready": True, "roi": 7.5},
]
df = pd.DataFrame(data)

# Criteria settings
MAX_PRICE = 1000000
MIN_SIZE = 600
MIN_ROI = 7.0
MIN_YEAR = 2019
ALLOWED_DEVELOPERS = ["Sobha", "Emaar"]

# Streamlit UI
st.title("🏢 Smart Deal Screener AI")
st.markdown("Filtering live real estate listings based on your custom criteria.")

# Filter logic
filtered = df[
    (df['price'] <= MAX_PRICE) &
    (df['size_sqft'] >= MIN_SIZE) &
    (df['bedrooms'] == 1) &
    (df['roi'] >= MIN_ROI) &
    (df['year_built'] > MIN_YEAR) &
    (df['developer'].isin(ALLOWED_DEVELOPERS)) &
    (df['ready'] == True)
]

st.subheader("🔍 Matching Properties")
if filtered.empty:
    st.warning("No deals match your criteria right now.")
else:
    st.dataframe(filtered.reset_index(drop=True))
