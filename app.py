import streamlit as st
import openai
from io import StringIO

# Function to summarize the document
def summarize_document(api_key, document):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",  # You might want to update the engine if a newer version is available
        prompt=f"Summarize the following document:\n\n{document}",
        temperature=0.5,
        max_tokens=250,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()

# Streamlit app layout
st.title('Document Summarizer')
st.write('This app uses OpenAI\'s GPT model to summarize documents. Please input your OpenAI API Key and upload a document.')

# Input for OpenAI API Key
api_key = st.text_input("OpenAI API Key", type="password")

# Document upload
uploaded_file = st.file_uploader("Choose a document", type=['txt', 'pdf', 'docx'])

if uploaded_file is not None and api_key:
    # Read the content of the file
    if uploaded_file.type == "text/plain":
        document = str(uploaded_file.read(), "utf-8")
    else:
        st.write("Currently, only text files are supported.")
        document = ""

    if document:
        # Summarize document
        summary = summarize_document(api_key, document)
        st.write("Summary:")
        st.write(summary)
else:
    st.write("Please upload a document and enter your API key to get a summary.")

