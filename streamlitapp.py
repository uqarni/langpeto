import streamlit as st
import os
import openai

st.title("Ideator Bot")

#ask if they have an idea already

#ask their job

#ask their hobby

#ask 

if uploaded_file is not None:
    with open("text.txt","wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded")

user_question = st.text_input(
    "Enter Your Question : ",
    placeholder = "Cyanobacteria can perform photosynthetsis , are they considered as plants?",
)

if st.button("Tell me about it", type = "primary"):
    loader = TextLoader('text.txt')
    index = VectorstoreIndexCreator().from_loaders([loader])
    query = user_question
    answer = index.query_with_sources(query)
    st.success(answer['answer'])