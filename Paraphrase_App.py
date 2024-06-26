import streamlit as st
from transformers import pipeline

# Load the text summarization pipeline
summarizer = pipeline("summarization")

# Function to capitalize the first letter of each sentence
def capitalize_sentences(text):
    sentences = text.split(". ")
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]
    return ". ".join(capitalized_sentences)

# Streamlit app
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('https://img.freepik.com/free-photo/top-view-arrangement-with-gadgets-copy-space_23-2148847745.jpg'); /* Replace YOUR_IMAGE_URL with the direct link to your image */
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
  
   .stSuccess {{
        background-color: #f0f0f0; /* Light gray background */
        color: black !important; /* Ensures the text is black */
        font-weight: bold !important; /* Ensures the text is bold */
        border-radius: 4px; /* Optional: Rounds the corners of the box */
        padding: 10px; /* Optional: Adds space inside the box */
        margin-top: 5px; /* Optional: Adds space above the box */
    }}
    button.custom-summarize-button {{
        background-color: #4CAF50; /* Green background */
        color: white; /* White text */
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 8px;
    }}
    button.custom-summarize-button:hover {{
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Text Summarization App")

# Input field for user to input text
st.markdown("<h2 style='color: black; font-size: 20px; font-weight: bold;'>Enter Text To Summarize:</h2>", unsafe_allow_html=True)
text_input = st.text_area("", height=200)

# Custom HTML button for summarization
if st.markdown('<button class="custom-summarize-button">Summarize</button>', unsafe_allow_html=True):
    if text_input:
        # Display loading spinner
        with st.spinner("Summarizing..."):
            # Perform text summarization
            summary = summarizer(text_input, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
            
            # Capitalize the first letter of each sentence
            capitalized_summary = capitalize_sentences(summary)
            
            # Display the summarized output in a box
            st.subheader("Summary")
            st.success(capitalized_summary)
