import streamlit as st
import pandas as pd
import os

# Configuration & Security (Only two specific users)
st.set_page_config(page_title="Data Entry Portal")

# Simple Access Control
users = {"admin": "pass123", "partner": "pass456"}

def save_to_excel(new_data):
    file = 'responses.xlsx'
    if os.path.isfile(file):
        df = pd.read_excel(file)
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    else:
        df = pd.DataFrame([new_data])
    df.to_excel(file, index=False)

# --- FORM UI ---
st.title("📋 Response Template")

with st.form("input_form"):
    name = st.text_input("Full Name")
    
    # Radio Buttons (Single Choice)
    satisfaction = st.radio("How satisfied are you?", ("Very Good", "Neutral", "Poor"))
    
    # Checkboxes (Multiple Choice)
    services = st.multiselect("Which services did you use?", ["Consulting", "Support", "Development"])
    
    submitted = st.form_submit_button("Submit Response")
    
    if submitted:
        data = {
            "Name": name,
            "Satisfaction": satisfaction,
            "Services": ", ".join(services)
        }
        save_to_excel(data)
        st.success("Data submitted successfully!")

# --- BACKEND (Admin Only) ---
st.sidebar.title("Admin Access")
user_input = st.sidebar.text_input("Username")
pass_input = st.sidebar.text_input("Password", type="password")

if user_input in users and users[user_input] == pass_input:
    st.sidebar.success("Logged In")
    if os.path.isfile('responses.xlsx'):
        with open("responses.xlsx", "rb") as f:
            st.sidebar.download_button("📥 Download Excel Database", f, file_name="database.xlsx")