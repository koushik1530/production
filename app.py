import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(page_title="Purchasing Tracker", layout="wide")

# --- CUSTOM CSS FOR HORIZONTAL RADIO BUTTONS ---
st.markdown("""
    <style>
    .stRadio > div { flex-direction: row !important; }
    div.row-widget.stRadio > div > label { background-color: #f0f2f6; padding: 5px 15px; border-radius: 10px; margin-right: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📋 Purchasing Production Tracker")
st.write("Please fill out the form below. All fields are required.")

# --- FORM UI ---
with st.form("production_form"):
    
    # Example of Question -> Answer (Radio Buttons)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write("### Q1: Supplier Confirmation Received?")
    with col2:
        conf_received = st.radio("", ["Y", "N"], key="q1", label_visibility="collapsed")

    st.divider()

    # Question 2
    col3, col4 = st.columns([1, 2])
    with col3:
        st.write("### Q2: Mail Sent to Supplier?")
    with col4:
        mail_sent = st.radio("", ["Y", "N"], key="q2", label_visibility="collapsed")

    st.divider()

    # Standard Input Fields (Horizontal)
    cA, cB, cC = st.columns(3)
    supplier = cA.text_input("Supplier Name")
    po_no = cB.text_input("PO Number")
    activity = cC.selectbox("Activity Type", ["Due for Service", "Price updates", "Follow Ups", "Unconfirmed Orders"])

    remarks = st.text_area("Additional Remarks")

    submitted = st.form_submit_button("Submit Response")

    if submitted:
        # DATA STORAGE LOGIC
        # Note: To avoid data loss, connect this to Google Sheets or Zoho Sheet.
        st.success("Data captured! To ensure you don't lose this data after the app sleeps, connect your Google Sheet Secrets.")
