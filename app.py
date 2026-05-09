import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Streamlit page
st.title("🍔 AI Local Food Guide")

st.write("Ask me about local food places!")

# User input
user_input = st.text_input("Enter your question")

if st.button("Ask"):

    prompt = f"""
    You are a local food guide assistant.
    Help users find food suggestions, cafes,
    restaurants, and famous dishes.
    
    User question: {user_input}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message.content

    st.success(answer)
