import streamlit as st
import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI with API key
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    st.error("API key not found. Please set the GOOGLE_API_KEY environment variable.")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(history=[])

def get_gemini_response(question):
    try:
        response = chat.send_message(question, stream=True)
        collected_response = ""
        for chunk in response:
            collected_response += chunk.text
        return collected_response
    except Exception as e:
        st.error(f"Error fetching response: {e}")
        return None

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Chatbot", layout="wide")
st.markdown("""
    <style>
        .chat-box {
            border: 1px solid #ccc;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        .chat-history {
            max-height: 400px;
            overflow-y: auto;
            margin-bottom: 20px;
        }
        .bot-response {
            color: blue;
        }
        .user-input {
            color: green;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Gemini Chatbot")

# Initialize session state for chat history if it doesn't already exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Function to clear chat history
def clear_chat():
    st.session_state['chat_history'] = []

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Ask a Question")
    input_text = st.text_input("Input:", key="input")
    submit = st.button("Ask the question")
    
    if submit and input_text:
        with st.spinner('Waiting for response...'):
            response = get_gemini_response(input_text)
            time.sleep(2)  # Wait for 2 seconds to ensure response is completely collected
        if response:
            # Update chat history
            st.session_state['chat_history'].append(("You", input_text))
            st.session_state['chat_history'].append(("Bot", response))
            st.subheader("Response:")
            st.markdown(f"<div class='chat-box bot-response'>{response}</div>", unsafe_allow_html=True)

    # Display chat history
    st.subheader("Chat History")
    chat_history_container = st.container()
    with chat_history_container:
        for role, text in st.session_state['chat_history']:
            if role == "You":
                st.markdown(f"<div class='chat-box user-input'>{role}: {text}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='chat-box bot-response'>{role}: {text}</div>", unsafe_allow_html=True)
    
    # Clear chat button
    if st.button("Clear Chat"):
        clear_chat()

with col2:
    st.subheader("Instructions")
    st.markdown("""
        1. Enter your question in the input box.
        2. Click the "Ask the question" button.
        3. Wait for the response to be displayed.
        4. View the chat history below.
        5. Click "Clear Chat" to reset the chat history.
    """)
