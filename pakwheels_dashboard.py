import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(page_title="PakWheels Car Listings Dashboard", layout="wide")
st.title("PakWheels Used Cars Dashboard")
st.markdown("Analyze listings, prices, brands, and city-wise trends.")


@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_pakwheels_listings.csv")
    df['Brand'] = df['Title'].str.split().str[0]
    return df

df = load_data()


st.sidebar.header("Filters")
cities = st.sidebar.multiselect("Select Cities", sorted(df['City'].unique()), default=sorted(df['City'].unique())[:5])
brands = st.sidebar.multiselect("Select Car Brands", sorted(df['Brand'].unique()), default=sorted(df['Brand'].unique())[:5])

filtered_df = df[(df['City'].isin(cities)) & (df['Brand'].isin(brands))]


st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Listings", len(filtered_df))
col2.metric("Avg. Price (PKR)", f"{filtered_df['Price (PKR)'].mean():,.0f}")
col3.metric("Avg. Mileage (km)", f"{filtered_df['Mileage (km)'].mean():,.0f}")


# --- Best Listing Showcase ---
st.subheader("🌟 Best Value Listing")

# Define a scoring function: lowest price per km, newest year
filtered_df['Score'] = (
    (filtered_df['Price (PKR)'] / filtered_df['Mileage (km)']) * (2025 - filtered_df['Year'])
)

# Drop rows with missing or zero mileage to avoid divide by zero
filtered_df_nonzero = filtered_df[(filtered_df['Mileage (km)'] > 0) & (~filtered_df['Score'].isnull())]

if not filtered_df_nonzero.empty:
    best_listing = filtered_df_nonzero.sort_values('Score').iloc[0]
    st.markdown(f"### 🏆 **{best_listing['Title']}**")
    st.markdown(f"- **Price:** {best_listing['Price (PKR)']:,} PKR")
    st.markdown(f"- **Mileage:** {best_listing['Mileage (km)']:,} km")
    st.markdown(f"- **Year:** {best_listing['Year']}")
    st.markdown(f"- **Engine:** {best_listing['Engine (cc)']} cc")
    st.markdown(f"- **City:** {best_listing['City']}")
    st.markdown(f"- [View Listing]({best_listing['Listing URL']})")
    st.image(best_listing['Image URL'], width=400)
else:
    st.info("No eligible best listing found (check mileage and year data).")

st.subheader("Top Cities by Listings")
top_cities = filtered_df['City'].value_counts().head(10)
fig1, ax1 = plt.subplots()
sns.barplot(x=top_cities.values, y=top_cities.index, ax=ax1)
st.pyplot(fig1)

# Top Brands
st.subheader("Top Brands by Listings")
top_brands = filtered_df['Brand'].value_counts().head(10)
fig2, ax2 = plt.subplots()
sns.barplot(x=top_brands.values, y=top_brands.index, ax=ax2)
st.pyplot(fig2)

# Price Distribution
st.subheader("Price Distribution")
fig3, ax3 = plt.subplots()
sns.histplot(filtered_df['Price (PKR)'], bins=30, kde=True, ax=ax3)
st.pyplot(fig3)

# Price by City
st.subheader("Price Distribution by City")
fig4, ax4 = plt.subplots(figsize=(12, 6))
sns.boxplot(x='City', y='Price (PKR)', data=filtered_df, ax=ax4)
ax4.tick_params(axis='x', rotation=45)
st.pyplot(fig4)

# --- Raw Data Preview ---
st.subheader("Preview Cleaned Listings Data")
st.dataframe(filtered_df)

