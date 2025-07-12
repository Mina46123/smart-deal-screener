import streamlit as st
import pandas as pd

# --------------------
# Mocked Bayut-style Listings
# --------------------
data = [
    {
        "title": "1BR in JVC by Sobha",
        "price": 950000,
        "size_sqft": 710,
        "bedrooms": 1,
        "developer": "Sobha",
        "year_built": 2022,
        "ready": True,
        "roi": 7.4,
        "url": "https://www.bayut.com/property-details-123456.html"
    },
    {
        "title": "1BR in Arjan",
        "price": 880000,
        "size_sqft": 590,
        "bedrooms": 1,
        "developer": "Smaller Dev",
        "year_built": 2018,
        "ready": True,
        "roi": 7.1,
        "url": "https://www.bayut.com/property-details-654321.html"
    },
    {
        "title": "1BR by Emaar in Dubai Hills",
        "price": 990000,
        "size_sqft": 640,
        "bedrooms": 1,
        "developer": "Emaar",
        "year_built": 2021,
        "ready": True,
        "roi": 6.9,
        "url": "https://www.bayut.com/property-details-789012.html"
    },
    {
        "title": "1BR in Business Bay",
        "price": 1020000,
        "size_sqft": 720,
        "bedrooms": 1,
        "developer": "Emaar",
        "year_built": 2020,
        "ready": True,
        "roi": 7.5,
        "url": "https://www.bayut.com/property-details-345678.html"
    }
]

df = pd.DataFrame(data)

# --------------------
# Filter Criteria
# --------------------
MAX_PRICE = 1000000
MIN_SIZE = 600
MIN_ROI = 7.0
MIN_YEAR = 2019
ALLOWED_DEVELOPERS = ["Sobha", "Emaar"]

# --------------------
# Streamlit UI
# --------------------
st.title("🏠 Smart Deal Screener AI")
st.markdown("Filtering real estate listings based on your custom criteria.")

# Apply filters
filtered = df[
    (df['price'] <= MAX_PRICE) &
    (df['size_sqft'] >= MIN_SIZE) &
    (df['bedrooms'] == 1) &
    (df['roi'] >= MIN_ROI) &
    (df['year_built'] > MIN_YEAR) &
    (df['developer'].isin(ALLOWED_DEVELOPERS)) &
    (df['ready'] == True)
]

# Convert titles to clickable links
filtered['Listing'] = filtered.apply(lambda row: f"[{row['title']}]({row['url']})", axis=1)

# Display
st.subheader("🔍 Matching Properties")
if filtered.empty:
    st.warning("No deals match your criteria right now.")
else:
    for index, row in filtered.iterrows():
    st.markdown(f"""
    ### 🔗 [{row['title']}]({row['url']})
    - **Price:** AED {row['price']:,}
    - **Size:** {row['size_sqft']} sqft
    - **ROI:** {row['roi']}%
    - **Year Built:** {row['year_built']}
    - **Developer:** {row['developer']}
    ---
    """)

