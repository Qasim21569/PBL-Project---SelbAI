import streamlit as st
import google.generativeai as genai

def main():
    st.title("ShelbAI Chatbot")

    # Set up your API key
    genai.configure(api_key="AIzaSyCzCTQ3HxtwaM5VAmKz_r5oFFHU2l5qL_A")

    
    # User input prompt
    user_prompt = st.text_input("Enter your prompt:", "")

    if user_prompt:
        # Initialize Gemini model
        model = genai.GenerativeModel('gemini-pro')

        # Generate response
        response = model.generate_content(user_prompt)

        # Display response
        st.code(response.text, language="c")  # Assuming response is C code

if __name__ == "__main__":
    main()
