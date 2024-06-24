# Gemini Chatbot

This project implements a chatbot using Google Generative AI's Gemini 1.5 Flash model. The chatbot is hosted on a Streamlit web application and allows users to interact with the AI model by asking questions and receiving responses.

## Features

- User-friendly UI with input, response, and chat history sections.
- Streamed responses from the AI model for real-time interaction.
- Option to clear the chat history.
- Instructions for using the chatbot.

## Technologies Used

- **Streamlit**: A web application framework used to create the user interface.
- **Python**: The programming language used to develop the application.
- **Google Generative AI**: The AI model used to generate responses.
- **dotenv**: A Python library to load environment variables from a `.env` file.
- **Google Generative AI Python Client**: Used to interact with the Gemini 1.5 Flash model.

## How It Works

1. **Environment Setup**:
    - The application loads the API key from a `.env` file using the `dotenv` library.
    - The API key is used to configure the Google Generative AI client.

2. **Streamlit Application**:
    - The app initializes with a clean UI layout, including sections for user input, chatbot responses, and chat history.
    - The `get_gemini_response` function sends user questions to the AI model and streams the responses.

3. **User Interaction**:
    - Users enter their questions in the input box and click the "Ask the question" button.
    - The application displays a spinner while waiting for the AI's response.
    - Once the response is received, it is displayed in the UI, and the chat history is updated.

4. **Chat History**:
    - The chat history is stored in the session state and displayed in a scrollable container.
    - A "Clear Chat" button allows users to reset the chat history.

## Setup Instructions

1. **Clone the Repository**:
    ```sh
    git clone <repository_url>
    cd gemini-chatbot
    ```

2. **Install Dependencies**:
    ```sh
    pip install streamlit python-dotenv google-generativeai
    ```

3. **Create a `.env` File**:
    - Add your Google API key to the `.env` file:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

4. **Run the Application**:
    ```sh
    streamlit run app.py
    ```

## File Structure

- `app.py`: The main application file containing the Streamlit app code.
- `.env`: Environment file containing the Google API key.

## Usage Instructions

1. **Start the application** by running `streamlit run app.py`.
2. **Enter your question** in the input box.
3. **Click "Ask the question"** to send the question to the AI model.
4. **Wait for the response** to be displayed under the "Response" section.
5. **View the chat history** to see previous interactions.
6. **Click "Clear Chat"** to reset the chat history.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for providing an easy-to-use web app framework.
- [Google Generative AI](https://developers.generativeai.google/) for the powerful AI model.
- [dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.
