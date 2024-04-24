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
        background-color: #f0f0f0;
        color: black;
        font-weight: bold;
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
