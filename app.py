
import streamlit as st
import requests
import os
#from dotenv import load_dotenv

# Load environment variables
#load_dotenv()
#PAYMENT_PASSWORD = os.getenv("PAYMENT_PASSWORD")  # Fetch password from environment variable
PAYMENT_PASSWORD = st.secrets["PAYMENT_PASSWORD"]
# FastAPI Backend URL
#API_URL = "http://127.0.0.1:8000/submit-payment/"
API_URL = "https://backend-sirius-payment.vercel.app/submit-payment/"
# st.image("logo_sirius.jpeg", width=200)
st.title("Sirius Academy Payment System")

# Input Fields
#teacher_name = st.text_input("Teacher Name")
teacher_name = st.selectbox("Select Teacher", ["Abrar", "Hamja", "Araf","Rumman","Kuresh","Tanvir","Safat","Nafiz","Sakib","Junayed","Sajid"])
student_name = st.text_input("Student Name")
amount = st.number_input("Amount", min_value=0.0, value=3000.0, step=100.0, format="%.2f")
tag = st.selectbox("Select Batch", ["HSC26", "HSC25", "SSC26", "SSC27"])
password = st.text_input("Enter Password", type="password")  # Password input

if st.button("Submit Payment"):
    if password == PAYMENT_PASSWORD :  # Securely validate password
        # Prepare request payload
        data = {
            "teacher_name": teacher_name,
            "student_name": student_name,
            "amount": amount,
            "tag": tag
        }

        # Send POST request to FastAPI backend
        response = requests.post(API_URL, json=data)

        # Handle response
        if response.status_code == 200:
            st.success("✅ Payment saved successfully!")
        else:
            st.error("❌ Failed to save payment. Please try again.")
    else:
        st.error("🔒 Incorrect password! Access denied.")
        
# streamlit run app.py
# pip3 install streamlit requests pandas
# source venv/bin/activate  
# pip3 freeze > requirements.txt
# pip3 install --upgrade pip
# pip3 install python-dotenv

# pip3 install python-dotenv
