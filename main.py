import streamlit as st
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate

def generateResponse(input_text):
    llm = Ollama(model="phi3:mini")
    st.write_stream(llm.stream(input_text))


st.title("Langchain")
with st.form("my_form"):
    question = st.text_input("question", "why do you do what you do?")
    submit = st.form_submit_button("Submit")
    if submit:
        generateResponse(question)
