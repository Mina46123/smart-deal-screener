import streamlit as st
import pandas as pd
import datetime

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
# Sidebar Filters
# --------------------
st.sidebar.title("🔧 Filter Listings")
max_price = st.sidebar.slider("Max Price (AED)", min_value=500000, max_value=2000000, value=1000000, step=50000)
min_size = st.sidebar.slider("Min Size (sqft)", min_value=300, max_value=1200, value=600, step=50)
min_roi = st.sidebar.slider("Min ROI (%)", min_value=0.0, max_value=12.0, value=7.0, step=0.1)
min_year = st.sidebar.slider("Built After Year", min_value=2000, max_value=datetime.datetime.now().year, value=2019)
all_developers = sorted(df['developer'].unique())
selected_developers = st.sidebar.multiselect("Allowed Developers", options=all_developers, default=["Sobha", "Emaar"])
ready_only = st.sidebar.checkbox("Only Ready Units", value=True)

# --------------------
# Filter Logic
# --------------------
filtered = df[
    (df['price'] <= max_price) &
    (df['size_sqft'] >= min_size) &
    (df['roi'] >= min_roi) &
    (df['year_built'] > min_year) &
    (df['developer'].isin(selected_developers))
]

if ready_only:
    filtered = filtered[filtered['ready'] == True]

# --------------------
# UI Output
# --------------------
st.title("🏠 Smart Deal Screener AI")
st.markdown("Use the sidebar filters to screen real estate investment deals in Dubai.")

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
        - **Year Built:** {row['year_built']} ({datetime.datetime.now().year - row['year_built']} years old)
        - **Developer:** {row['developer']}
        ---
        """)
