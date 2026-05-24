import streamlit as st
from chatbot import ask_llm

st.title("LLM Vehicle Maintenance Assistant")

query = st.text_area("Enter Vehicle Problem")

if st.button("Analyze Issue"):

    result = ask_llm(query)

    st.write(result)