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
        background-image: url('https://www.google.com/url?sa=i&url=https%3A%2F%2Fowl.excelsior.edu%2Forc%2Fwhat-to-do-after-reading%2Fparaphrasing%2F&psig=AOvVaw0KM_A4oNruewquL3R3K-R1&ust=1714072453068000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCJCtrvjH24UDFQAAAAAdAAAAABAX'); /* Replace YOUR_IMAGE_URL with the direct link to your image */
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
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Text Summarization App")

# Input field for user to input text
st.markdown("<h2 style='color: black; font-size: 20px; font-weight: bold;'>Enter Text To Summarize:</h2>", unsafe_allow_html=True)
text_input = st.text_area("", height=100)

# Summarization button
if st.button("Summarize"):
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
