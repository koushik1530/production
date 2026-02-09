import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Page Config
st.set_page_config(page_title="Production Tracker Pro", layout="wide")

# --- CUSTOM CSS FOR HORIZONTAL LAYOUT ---
st.markdown("""
    <style>
    .stRadio > div { flex-direction: row !important; gap: 30px; }
    div.row-widget.stRadio > div > label { background-color: #f0f2f6; padding: 5px 20px; border-radius: 10px; border: 1px solid #d1d3d8; }
    .question-text { font-size: 1.1rem; font-weight: bold; color: #1f2937; margin-bottom: 0px; padding-top: 10px; }
    .stNumberInput, .stTextInput, .stDateInput, .stSelectbox { padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Admin Credentials
users = {"admin": "pass123", "partner": "pass456"}

def save_to_excel(new_data):
    file = 'responses.xlsx'
    if os.path.isfile(file):
        df = pd.read_excel(file)
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    else:
        df = pd.DataFrame([new_data])
    df.to_excel(file, index=False)

st.title("🏭 Purchasing Production Tracker")


# --- FORM UI ---
with st.form("production_tracker_form", clear_on_submit=True):
    
    # Q2: Production Date (Date Picker)
    colA1, colA2 = st.columns([1, 2])
    with colA1: st.markdown('<p class="question-text">Q2: Production Date</p>', unsafe_allow_html=True)
    with colA2: prod_date = st.date_input("prod_date", label_visibility="collapsed")

    st.divider()

    # Q3: Supplier ID (Text + Numbers)
    colB1, colB2 = st.columns([1, 2])
    with colB1: st.markdown('<p class="question-text">Q3: Supplier ID</p>', unsafe_allow_html=True)
    with colB2: supplier_id = st.text_input("supplier_id", label_visibility="collapsed")

    st.divider()

    # Q4: PO ID (Number Input)
    colC1, colC2 = st.columns([1, 2])
    with colC1: st.markdown('<p class="question-text">Q4: PO ID</p>', unsafe_allow_html=True)
    with colC2: po_id = st.number_input("po_id", step=1, value=0, label_visibility="collapsed")

    st.divider()

    # Q5: Order Place Date (Date Picker)
    colD1, colD2 = st.columns([1, 2])
    with colD1: st.markdown('<p class="question-text">Q5: Order Place Date</p>', unsafe_allow_html=True)
    with colD2: order_date = st.date_input("order_date", label_visibility="collapsed")

    st.divider()

    # Q6: Activity Type (Dropdown)
    colE1, colE2 = st.columns([1, 2])
    with colE1: st.markdown('<p class="question-text">Q6: Activity Type</p>', unsafe_allow_html=True)
    with colE2: activity = st.selectbox("activity", ["Follow up", "PO release", "Cargoes"], label_visibility="collapsed")

    st.divider()

    # Q7: ORG (Text Input)
    colF1, colF2 = st.columns([1, 2])
    with colF1: st.markdown('<p class="question-text">Q7: ORG</p>', unsafe_allow_html=True)
    with colF2: org = st.text_input("org", label_visibility="collapsed")

    st.divider()

    # Q8: Supplier Confirmation Received (Radio YES/NO/N/A)
    colG1, colG2 = st.columns([1, 2])
    with colG1: st.markdown('<p class="question-text">Q8: Supplier Confirmation Received?</p>', unsafe_allow_html=True)
    with colG2: q8_ans = st.radio("q8", ["YES", "NO", "N/A"], key="q8", label_visibility="collapsed")

    st.divider()

    # Q9: Mail Sent (Radio YES/NO/N/A)
    colH1, colH2 = st.columns([1, 2])
    with colH1: st.markdown('<p class="question-text">Q9: Mail Sent?</p>', unsafe_allow_html=True)
    with colH2: q9_ans = st.radio("q9", ["YES", "NO", "N/A"], key="q9", label_visibility="collapsed")

    st.divider()

    # Q10 & Q11: ETA and Remarks
    colI1, colI2 = st.columns([1, 2])
    with colI1: st.markdown('<p class="question-text">Q10: ETA</p>', unsafe_allow_html=True)
    with colI2: eta = st.text_input("eta", label_visibility="collapsed")

    colJ1, colJ2 = st.columns([1, 2])
    with colJ1: st.markdown('<p class="question-text">Q11: Remarks</p>', unsafe_allow_html=True)
    with colJ2: remarks = st.text_input("remarks", label_visibility="collapsed")

    st.divider()

    # Q12 - Q15: Status and Follow Ups (Text Inputs)
    st.subheader("NAV & Follow-Up Status")
    
    q12_1, q12_2 = st.columns([1, 2])
    with q12_1: st.markdown('<p class="question-text">Q12: NAV Status</p>', unsafe_allow_html=True)
    with q12_2: nav_status = st.text_input("nav", label_visibility="collapsed")

    q13_1, q13_2 = st.columns([1, 2])
    with q13_1: st.markdown('<p class="question-text">Q13: FUP 1 DATE with Remarks 1</p>', unsafe_allow_html=True)
    with q13_2: fup1 = st.text_input("fup1", label_visibility="collapsed")

    q14_1, q14_2 = st.columns([1, 2])
    with q14_1: st.markdown('<p class="question-text">Q14: FUP 2 Date with Remarks</p>', unsafe_allow_html=True)
    with q14_2: fup2 = st.text_input("fup2", label_visibility="collapsed")

    q15_1, q15_2 = st.columns([1, 2])
    with q15_1: st.markdown('<p class="question-text">Q15: FUP 3 Date with Remarks</p>', unsafe_allow_html=True)
    with q15_2: fup3 = st.text_input("fup3", label_visibility="collapsed")

    # Submit Button
    submitted = st.form_submit_button("Submit Production Data")

    if submitted:
        new_entry = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Production Date": str(prod_date),
            "Supplier ID": supplier_id,
            "PO ID": po_id,
            "Order Place Date": str(order_date),
            "Activity Type": activity,
            "ORG": org,
            "Supplier Confirmation": q8_ans,
            "Mail Sent": q9_ans,
            "ETA": eta,
            "Remarks": remarks,
            "NAV Status": nav_status,
            "FUP 1": fup1,
            "FUP 2": fup2,
            "FUP 3": fup3
        }
        save_to_excel(new_entry)
        st.success("✅ Data saved successfully to the database!")

# --- ADMIN SIDEBAR ---
st.sidebar.title("🔐 Admin Access")
u_name = st.sidebar.text_input("Username")
p_word = st.sidebar.text_input("Password", type="password")

if u_name in users and users[u_name] == p_word:
    st.sidebar.success("Logged In")
    if os.path.isfile('responses.xlsx'):
        with open("responses.xlsx", "rb") as f:
            st.sidebar.download_button("📥 Download Excel Sheet", f, file_name="Production_Tracker.xlsx")

