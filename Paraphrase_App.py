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
        background-image: url('data:image/jpeg;base64,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'); /* Replace YOUR_IMAGE_URL with the direct link to your image */
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
