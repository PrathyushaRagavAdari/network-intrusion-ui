import streamlit as st

st.title("Network Intrusion Detection")
st.write("Upload a network traffic log to analyze anomalies.")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    st.write("Processing file...")