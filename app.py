import streamlit as st
from google import genai

# Setup the AI Client using Streamlit Secrets for safe deployment
# This will pull the 'GOOGLE_API_KEY' you saved in the cloud settings
client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

# Build the Web Page UI
st.title("AI Code Reviewer & Optimizer 🕵️‍♂️")
st.markdown("Paste your code below to automatically find bugs and get optimization suggestions.")

# Create the text input box
code_input = st.text_area("Enter your code:", height=250)

# Create the submit button
if st.button("Review My Code"):
    if code_input.strip():
        with st.spinner("Analyzing code..."):
            # The prompt telling the AI exactly what to do
            prompt = f"Act as an expert code auditor. Identify any logical bugs or inefficiencies in this code. Provide the corrected code and a 3-bullet-point explanation:\n\n{code_input}"
            
            try:
                # Send the prompt to the new Gemini 3.5 Flash model
                response = client.models.generate_content(
                    model='gemini-3.5-flash',
                    contents=prompt
                )
                
                # Display the AI's response on the website
                st.markdown("### Review Results")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please paste some code first!")