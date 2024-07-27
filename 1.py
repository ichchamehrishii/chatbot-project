# import streamlit as st #for ui
# import os
# from dotenv import load_dotenv #to get env variables loaded into the application
# load_dotenv() #loading of all the env variable

# import google.generativeai as genai

# #genai config of api
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # initialise the model
# model = genai.GenerativeModel('gemini-pro')

# # define a function to generate response from llm
# def get_gemini_response(ques):
#     resp = model.generate_content(ques)
#     return resp.text

# # setting up streamlit app
# st.set_page_config(
#     page_title="Gemini pro Q/A project",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # setting up header
# st.header("Gemini Q/A app")
# # st.title

# # input
# question = st.text_input("Ask a question: ")

# #submit button
# if st.button("Submit"):
#     response = get_gemini_response(question)
#     st.write("*User*:", question)
#     st.write("*Bot*:", response)


import streamlit as st  # for UI
import os
from dotenv import load_dotenv  # to get env variables loaded into the application

# Load environment variables
load_dotenv()

import google.generativeai as genai

# Configure API for Generative AI
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("GOOGLE_API_KEY not found in environment variables.")
else:
    genai.configure(api_key=api_key)

    # Initialize the model
    model = genai.GenerativeModel('gemini-pro')

    # Define a function to generate responses from the model
    def get_gemini_response(ques):
        try:
            resp = model.generate_content(ques)
            return resp.text
        except Exception as e:
            st.error(f"Error generating response: {e}")
            return "Error generating response"

    # Set up the Streamlit app
    st.set_page_config(
        page_title="Gemini Pro Q/A Project",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Header
    st.header("Gemini Q/A App")

    # Input
    question = st.text_input("Ask a question:")

    # Submit button
    if st.button("Submit"):
        if question:
            response = get_gemini_response(question)
            st.write("*User*:", question)
            st.write("*Bot*:", response)
        else:
            st.warning("Please enter a question before submitting.")
