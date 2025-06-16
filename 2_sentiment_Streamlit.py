import streamlit as st
import ollama
import pandas as pd
from langchain_ollama.llms import OllamaLLM
from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(
    page_title="AI Book Butler"
)

ollama_model = "llama3.2"

prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a sentiment analysis expert. Analyze the sentiment of the given text"),
            ("human", "Analyze the sentiment of the following text: {text}")
        ])

def generate_response(input_text):
    model = ChatOllama(model=ollama_model, temperature=0.7)
    output_parser = StrOutputParser()
    chain = prompt | model | output_parser
    result = chain.invoke({"text": text})
    st.info(result)

with st.form("chat_form"):
    text = st.text_area(
        "Welcome, I'm AIBookButler running " + ollama_model + " \n. Please tell me a passage from a book you'd like me to analyze."
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)

