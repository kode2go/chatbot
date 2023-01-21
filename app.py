import openai
import streamlit as st
from datetime import datetime
import pandas as pd

openai.api_key = st.secrets["api_secret"]
df = pd.DataFrame(columns=['Timestamp', 'Question', 'Response'])



"""
# Welcome to My Hospital Chatbot!

Feel free to ask any questions below:

"""

chatbot_input = st.text_input('Ask a question?','What is an angiogram?')

if st.button('Submit'):
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y_%H:%M:%S")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=chatbot_input,
        temperature=0.5
    )

    answer = response["choices"][0]["text"]
    st.write(answer)
    print(answer)

#     new_row = pd.Series([timestampStr, chatbot_input, answer], index=df.columns)
#     df = df.append(new_row,ignore_index=True) 
#     df.to_csv('submissions.csv', mode='a', index=False, header=False)
