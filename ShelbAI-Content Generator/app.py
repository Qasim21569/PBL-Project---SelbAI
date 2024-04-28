import os
import streamlit as st
from streamlit_chat import message
from google.generativeai import GenerativeModel

# Set up your API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyCzCTQ3HxtwaM5VAmKz_r5oFFHU2l5qL_A"

st.title("Gemini Chatbot")

# Print the API key to check if it's set correctly
print("API key in app.py:", os.getenv('GOOGLE_API_KEY'))

# Initialize 'responses' key in session state if not present
if 'responses' not in st.session_state:
    st.session_state['responses'] = []

def generate_response(prompt):
    # Initialize Gemini model without specifying API key
    model = GenerativeModel('gemini-pro')
    # Generate response
    response = model.generate_content(prompt)
    return response.text

def user_input():
    input_text = st.text_input("Enter your prompt:")
    return input_text

user_text = user_input()

if user_text:
    output = generate_response(user_text)
    st.session_state['responses'].append({'user': user_text, 'bot': output})

if st.session_state['responses']:
    for chat in reversed(st.session_state['responses']):
        message(chat['user'], is_user=True)
        message(chat['bot'])
