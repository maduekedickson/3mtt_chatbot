import streamlit as st
import google.generativeai as genai
import time

# Initialize Gemini Pro API

# Set the API key directly
genai.configure(api_key="AIzaSyCbknlcRQiRQ5B1JtodNeCFHJeAxYJFD0E")




model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Welcome to the General Knowledge Chatbot! Ask me anything."},
    ]
)

# Streamlit App
st.title("🌐 General Knowledge Chatbot")

st.text("3mtt capstone project")

# Input Section
user_input = st.text_input("Type your question below and press Enter:")

# Placeholder for chatbot response
response_placeholder = st.empty()

if user_input:
    # Display "Typing..." message
    with response_placeholder:
        st.write("🤖 Typing...")
    
    # Simulate delay
    time.sleep(2)
    
    # Get response from Gemini API
    response = chat.send_message(user_input)
    
    # Display the response
    response_placeholder.write(f"🤖: {response.text}")
