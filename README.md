# chatbot-project

Gemini Q/A Chatbot
Welcome to the Gemini Q/A Chatbot project! This is a simple chatbot application built using Python, Streamlit, and Google's Gemini API. The application allows users to ask questions and receive responses powered by the Gemini generative AI model.

Features
Interactive User Interface: A web-based UI created with Streamlit for user-friendly interaction.
Generative AI: Utilizes Google's Gemini API to generate responses to user queries.
Prerequisites
To run this project, you'll need the following:

Python 3.x
A Google Cloud account with access to the Gemini API
Streamlit
python-dotenv for loading environment variables


installation:
streamlit
langchain
google-generativeai
python-dotenv
langchain-community
langchain-google-genai
PyPDF2

How It Works
Streamlit Setup: The application uses Streamlit for creating a simple web interface where users can input their questions.
API Interaction: When a question is submitted, it is sent to the Gemini API using the google.generativeai library.
Response Generation: The API generates a response based on the input question, which is then displayed back to the user.
Code Explanation
Dependencies: Imports necessary libraries and configurations.
API Configuration: Configures the Gemini API using an API key from environment variables.
Streamlit UI: Sets up the page layout, header, input field, and submit button for user interaction.
Response Handling: Uses a function to generate responses from the Gemini model and displays them in the UI.
Troubleshooting
API Key Issues: Ensure that your API key is correctly set in the .env file.
Dependency Errors: Make sure all required libraries are installed and up-to-date.
Streamlit Errors: Check for any errors in the terminal for hints on what might be wrong.
