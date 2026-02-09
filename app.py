import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Page Config
st.set_page_config(page_title="Production Tracker Pro", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stRadio > div { flex-direction: row !important; gap: 30px; }
    div.row-widget.stRadio > div > label { background-color: #f0f2f6; padding: 5px 20px; border-radius: 10px; border: 1px solid #d1d3d8; }
    .question-text { font-size: 1.1rem; font-weight: bold; color: #1f2937; margin-bottom: 0px; padding-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

users = {"admin": "pass123", "partner": "pass456"}

def save_to_excel(new_data):
    file = 'responses.xlsx'
    # Define exact column order for the Excel Output
    column_order = [
        "Timestamp", "Name", "Production Date", "Supplier ID", "PO ID", 
        "Order Place Date", "Activity Type", "ORG", 
        "Supplier Confirmation Received", "Mail Sent", "ETA", "Remarks", 
        "NAV Status", "FUP 1", "FUP 2", "FUP 3"
    ]
    
    new_df = pd.DataFrame([new_data])
    
    if os.path.isfile(file):
        df = pd.read_excel(file)
        df = pd.concat([df, new_df], ignore_index=True)
    else:
        df = new_df
    
    # Reorder columns to match requirement
    df = df.reindex(columns=column_order)
    df.to_excel(file, index=False)

st.title("🏭 Purchasing Production Tracker")

# --- FORM UI ---
with st.form("production_tracker_form", clear_on_submit=True):
    
    # Q1: Name (New)
    colZ1, colZ2 = st.columns([1, 2])
    with colZ1: st.markdown('<p class="question-text">Q1: Your Name</p>', unsafe_allow_html=True)
    with colZ2: user_name = st.text_input("user_name", label_visibility="collapsed")

    st.divider()

    # Q2: Production Date
    colA1, colA2 = st.columns([1, 2])
    with colA1: st.markdown('<p class="question-text">Q2: Production Date</p>', unsafe_allow_html=True)
    with colA2: prod_date = st.date_input("prod_date", label_visibility="collapsed")

    st.divider()

    # Q3: Supplier ID
    colB1, colB2 = st.columns([1, 2])
    with colB1: st.markdown('<p class="question-text">Q3: Supplier ID</p>', unsafe_allow_html=True)
    with colB2: supplier_id = st.text_input("supplier_id", label_visibility="collapsed")

    st.divider()

    # Q4: PO ID
    colC1, colC2 = st.columns([1, 2])
    with colC1: st.markdown('<p class="question-text">Q4: PO ID</p>', unsafe_allow_html=True)
    with colC2: po_id = st.number_input("po_id", step=1, value=0, label_visibility="collapsed")

    st.divider()

    # Q5: Order Place Date
    colD1, colD2 = st.columns([1, 2])
    with colD1: st.markdown('<p class="question-text">Q5: Order Place Date</p>', unsafe_allow_html=True)
    with colD2: order_date = st.date_input("order_date", label_visibility="collapsed")

    st.divider()

    # Q6: Activity Type
    colE1, colE2 = st.columns([1, 2])
    with colE1: st.markdown('<p class="question-text">Q6: Activity Type</p>', unsafe_allow_html=True)
    with colE2: activity = st.selectbox("activity", ["Follow up", "PO release", "Cargoes"], label_visibility="collapsed")

    st.divider()

    # Q7: ORG
    colF1, colF2 = st.columns([1, 2])
    with colF1: st.markdown('<p class="question-text">Q7: ORG</p>', unsafe_allow_html=True)
    with colF2: org = st.text_input("org", label_visibility="collapsed")

    st.divider()

    # Q8: Supplier Confirmation Received (index=None for no default selection)
    colG1, colG2 = st.columns([1, 2])
    with colG1: st.markdown('<p class="question-text">Q8: Supplier Confirmation Received?</p>', unsafe_allow_html=True)
    with colG2: q8_ans = st.radio("q8", ["YES", "NO", "N/A"], index=None, key="q8", label_visibility="collapsed")

    st.divider()

    # Q9: Mail Sent (index=None for no default selection)
    colH1, colH2 = st.columns([1, 2])
    with colH1: st.markdown('<p class="question-text">Q9: Mail Sent?</p>', unsafe_allow_html=True)
    with colH2: q9_ans = st.radio("q9", ["YES", "NO", "N/A"], index=None, key="q9", label_visibility="collapsed")

    st.divider()

    # Q10 - Q15 (Remaining Fields)
    st.subheader("Additional Information")
    
    colI1, colI2 = st.columns([1, 2])
    with colI1: st.markdown('<p class="question-text">Q10: ETA</p>', unsafe_allow_html=True)
    with colI2: order_date = st.date_input("ETA", label_visibility="collapsed")

    colJ1, colJ2 = st.columns([1, 2])
    with colJ1: st.markdown('<p class="question-text">Q11: Remarks</p>', unsafe_allow_html=True)
    with colJ2: remarks = st.text_input("remarks", label_visibility="collapsed")

    colK1, colK2 = st.columns([1, 2])
    with colK1: st.markdown('<p class="question-text">Q12: NAV Status</p>', unsafe_allow_html=True)
    with colK2: nav = st.text_input("nav", label_visibility="collapsed")

    colL1, colL2 = st.columns([1, 2])
    with colL1: st.markdown('<p class="question-text">Q13: FUP 1 DATE with Remarks</p>', unsafe_allow_html=True)
    with colL2: fup1 = st.text_input("fup1", label_visibility="collapsed")

    colM1, colM2 = st.columns([1, 2])
    with colM1: st.markdown('<p class="question-text">Q14: FUP 2 Date with Remarks</p>', unsafe_allow_html=True)
    with colM2: fup2 = st.text_input("fup2", label_visibility="collapsed")

    colN1, colN2 = st.columns([1, 2])
    with colN1: st.markdown('<p class="question-text">Q15: FUP 3 Date with Remarks</p>', unsafe_allow_html=True)
    with colN2: fup3 = st.text_input("fup3", label_visibility="collapsed")

    # Submit
    submitted = st.form_submit_button("Submit Production Data")

    if submitted:
        if q8_ans is None or q9_ans is None:
            st.error("Please answer the radio button questions (Q8 & Q9) before submitting.")
        else:
            new_entry = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": user_name,
                "Production Date": str(prod_date),
                "Supplier ID": supplier_id,
                "PO ID": po_id,
                "Order Place Date": str(order_date),
                "Activity Type": activity,
                "ORG": org,
                "Supplier Confirmation Received": q8_ans,
                "Mail Sent": q9_ans,
                "ETA": eta,
                "Remarks": remarks,
                "NAV Status": nav,
                "FUP 1": fup1,
                "FUP 2": fup2,
                "FUP 3": fup3
            }
            save_to_excel(new_entry)
            st.success("✅ Data saved! Form cleared.")

# --- SIDEBAR ---
st.sidebar.title("🔐 Admin Access")
u_name = st.sidebar.text_input("Username")
p_word = st.sidebar.text_input("Password", type="password")

if u_name in users and users[u_name] == p_word:
    st.sidebar.success("Logged In")
    if os.path.isfile('responses.xlsx'):
        with open("responses.xlsx", "rb") as f:
            st.sidebar.download_button("📥 Download Excel Sheet", f, file_name="Production_Tracker_Report.xlsx")


