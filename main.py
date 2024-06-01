import streamlit as st
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate

llm = Ollama(model="phi3:mini")

def generateResponse(input_text):
    st.write_stream(llm.stream(input_text))

def generatePrompt(parameters: list):
    generate_prompt_template = """
    You are a prompt generator working for the langchain community. You will be given a python list
    of characteristics that a prompt should have which will invoke a particular tone and style of response
    from the langauge model. The python list provided is:
    {parameters}
    based on these parameters develop the most effective prompt you can.
    """

    prompt = PromptTemplate.from_template(generate_prompt_template)
    output = (prompt | llm).stream(parameters)
    st.write_stream(output)


st.title("Langchain")
with st.form("prompt_generator"):  
    st.markdown("### Prompt generator")
    options = st.multiselect(
    "select parameters",
    ["Sarcastic", "Positive", "Straightforward", "Mocking"],
    ["Positive", "Straightforward"])
    prompt_gen_submit = st.form_submit_button("Submit")
    if prompt_gen_submit:
        generatePrompt(options)

st.subheader(" ")

with st.form("prompt_form"):
    st.markdown("### Enter your prompt")
    prompt_question = st.text_input("enter the prompt you wanna use for the rest of the session")
    prompt_submit = st.form_submit_button("Submit")
    if prompt_submit:
        pass

with st.form("my_form"):
    st.markdown("### enter your question")
    question = st.text_input("question", "why do you do what you do?")
    submit = st.form_submit_button("Submit")
    if submit:
        generateResponse(question)
