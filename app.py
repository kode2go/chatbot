import openai
import streamlit as st

openai.api_key = "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"

"""
# Welcome to My Hospital Chatbot!

Feel free to ask any questions below:

"""

chatbot_input = st.text_input('What is an angiogram?')

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=chatbot_input,
    temperature=0.5
)

answer = response["choices"][0]["text"]
st.write(answer)
print(answer)
