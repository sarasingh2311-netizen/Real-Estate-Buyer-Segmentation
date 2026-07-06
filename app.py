import streamlit as st
import pandas as pd

st.set_page_config(page_title="Real Estate Buyer Segmentation", layout="wide")

st.title("🏠 Real Estate Buyer Segmentation")

# Load datasets
clients = pd.read_csv("clients.csv")
properties = pd.read_csv("properties(1).csv")

# Merge datasets
df = pd.merge(
    clients,
    properties,
    left_on="client_id",
    right_on="client_ref",
    how="inner"
)

st.subheader("Merged Dataset")
st.dataframe(df.head())

st.subheader("Dataset Information")
st.write(f"Rows: {df.shape[0]}")
st.write(f"Columns: {df.shape[1]}")

st.subheader("Client Type Distribution")
st.bar_chart(df["client_type"].value_counts())

if "country" in df.columns:
    st.subheader("Country Distribution")
    st.bar_chart(df["country"].value_counts())

st.success("Buyer Segmentation Project Loaded Successfully!")
