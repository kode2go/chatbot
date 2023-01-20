import openai
import streamlit as st

openai.api_key = "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"

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt='What is an angiogram?',
    temperature=0.5
)

answer = response["choices"][0]["text"]
st.write(answer)
print(answer)
