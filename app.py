import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Page Config
st.set_page_config(page_title="Purchasing Tracker", layout="wide")

# --- CUSTOM CSS FOR HORIZONTAL RADIO BUTTONS ---
st.markdown("""
    <style>
    .stRadio > div { flex-direction: row !important; gap: 20px; }
    div.row-widget.stRadio > div > label { background-color: #f0f2f6; padding: 5px 15px; border-radius: 10px; }
    .question-text { font-size: 1.2rem; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Simple Access Control for the sidebar download
users = {"admin": "pass123", "partner": "pass456"}

def save_to_excel(new_data):
    file = 'responses.xlsx'
    if os.path.isfile(file):
        df = pd.read_excel(file)
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    else:
        df = pd.DataFrame([new_data])
    df.to_excel(file, index=False)

st.title("📋 Purchasing Production Tracker")

# --- FORM UI ---
with st.form("production_form"):
    
    # Q1
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<p class="question-text">Q1: Supplier Confirmation Received?</p>', unsafe_allow_html=True)
    with col2:
        q1_ans = st.radio("q1", ["YES", "NO", "N/A"], key="q1", label_visibility="collapsed")

    st.divider()

    # Q2
    col3, col4 = st.columns([1, 2])
    with col3:
        st.markdown('<p class="question-text">Q2: Mail Sent to Supplier?</p>', unsafe_allow_html=True)
    with col4:
        q2_ans = st.radio("q2", ["YES", "NO", "N/A"], key="q2", label_visibility="collapsed")

    st.divider()

    # Q3
    col5, col6 = st.columns([1, 2])
    with col5:
        st.markdown('<p class="question-text">Q3: Production Status Verified?</p>', unsafe_allow_html=True)
    with col6:
        q3_ans = st.radio("q3", ["YES", "NO", "N/A"], key="q3", label_visibility="collapsed")

    st.divider()

    # Standard Input Fields
    cA, cB, cC = st.columns(3)
    supplier = cA.text_input("Supplier Name")
    po_no = cB.text_input("PO Number")
    activity = cC.selectbox("Activity Type", ["Due for Service", "Price updates", "Follow Ups", "Unconfirmed Orders"])

    remarks = st.text_area("Additional Remarks")

    submitted = st.form_submit_button("Submit Response")

    if submitted:
        data = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Q1_Confirmation": q1_ans,
            "Q2_MailSent": q2_ans,
            "Q3_Status": q3_ans,
            "Supplier": supplier,
            "PO_Number": po_no,
            "Activity": activity,
            "Remarks": remarks
        }
        save_to_excel(data)
        st.success("✅ Data captured successfully!")

# --- ADMIN SIDEBAR ---
st.sidebar.title("🔐 Admin Access")
u_input = st.sidebar.text_input("Username")
p_input = st.sidebar.text_input("Password", type="password")

if u_input in users and users[u_input] == p_input:
    st.sidebar.success("Logged In")
    if os.path.isfile('responses.xlsx'):
        with open("responses.xlsx", "rb") as f:
            st.sidebar.download_button("📥 Download Excel Database", f, file_name="production_report.xlsx")
