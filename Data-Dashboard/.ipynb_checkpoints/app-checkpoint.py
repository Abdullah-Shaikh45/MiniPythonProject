import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_csv('data/owid-covid-data.csv')
df['date'] = pd.to_datetime(df['date'])

# Sidebar Filters
st.sidebar.title("Dashboard Filters")
countries = sorted(df['location'].unique())
selected_country = st.sidebar.selectbox("Select a country", countries)

# Filter by Selected Country
filtered_df = df[df['location'] == selected_country]

# Dashboard
st.title("COVID-19 Dashboard")
st.subheader(f"New COVID Cases in {selected_country}")

fig = px.line(filtered_df, x='date', y='new_cases', title="", labels={'new_cases': 'New Cases'})
st.plotly_chart(fig)

# Data Preview
st.markdown("### Raw Data Preview")
st.dataframe(filtered_df.tail(100))
