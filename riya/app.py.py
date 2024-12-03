import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Initialize Groq API key
api_key = os.getenv("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")

# Define the Groq client
client = Groq(api_key=api_key)

# Streamlit UI
st.title("Cloth Recommendations")

# User input
topic = st.text_input("Enter a clothing style or type you are interested in:")

# When the user submits a topic
if st.button("Get Recommendations"):
    if topic:
        # Prepare the request payload
        messages = [
            {
                "role": "user",
                "content": f"I am looking for clothing recommendations for the style/type: {topic}. Please provide a list of clothing items, their descriptions, and where they could be worn."
            }
        ]

        # Send a request to the Groq API
        try:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model="llama3-8b-8192"  # Replace with the desired model
            )

            recommendations = chat_completion.choices[0].message.content
            st.write("### Clothing Recommendations:")
            st.write(recommendations)
        except Exception as e:
            st.write("Error: Could not fetch recommendations.")
            st.write(str(e))
    else:
        st.write("Please enter a clothing style or type to get recommendations.")