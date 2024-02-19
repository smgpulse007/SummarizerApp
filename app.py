import streamlit as st
import openai

# Function to summarize the document or text
def summarize_document(api_key, document_text):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",  # Update the engine if a newer version is available
        prompt=f"Summarize the following document:\n\n{document_text}",
        temperature=0.5,
        max_tokens=250,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()

# Streamlit app layout
st.title('Document and Text Summarizer')
st.write('This app uses OpenAI\'s GPT model to summarize documents or text. Please input your OpenAI API Key and upload a document or paste the text below.')

# Display an image
image_path = 'landing_page_image.jpg'  # Replace 'landing_page_image.jpg' with your image file name
st.image(image_path, caption='Transforming Information with AI: From Text Overload to Concise Summaries', use_column_width=True)

# Input for OpenAI API Key
api_key = st.text_input("OpenAI API Key", type="password")

# Tabs for Document Upload and Text Input
tab1, tab2 = st.tabs(["Upload Document", "Paste Text"])

with tab1:
    # Document upload
    uploaded_file = st.file_uploader("Choose a document", type=['txt', 'pdf', 'docx'])
    document_text = ""
    if uploaded_file is not None:
        # Read the content of the file
        document_text = str(uploaded_file.read(), "utf-8")

with tab2:
    # Text box for copy-pasting text
    pasted_text = st.text_area("Paste your text here")
    if pasted_text:
        document_text = pasted_text

if document_text and api_key:
    # Summarize document or text
    summary = summarize_document(api_key, document_text)
    st.subheader("Summary:")
    st.write(summary)
else:
    st.write("Please upload a document, paste text, and enter your API key to get a summary.")
