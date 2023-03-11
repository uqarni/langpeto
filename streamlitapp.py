import streamlit as st
import webbrowser


st.title("Ideator Bot")

#ask if they have an idea already and save the user's answer
question = "Do you have an app idea already?"
answer_options = ["Yes, I have an app idea already.", "No, I don't have an app idea already."]
answer = st.radio(question, answer_options)

# conditional component once they click Next Step
if st.button ("Next Step"):
    #if they chose yes, take them to an external site
    if answer == answer_options[0]:
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=xvFZjo5PgG0")
    #if they chose no, ask them what their job and type thier job to them
    if answer == answer_options[1]:
        st.success("No problem! Let's ideate. First, what job do you work?")
        job = st.text_input("Chat window", key = "job_input")
        
        if st.session_state.job_input:
            if st.session_state.job_input.endswith("\n"):
                st.write("your job is "+job)
        



#ask their hobby

#ask 

# if uploaded_file is not None:
#     with open("text.txt","wb") as f:
#         f.write(uploaded_file.getbuffer())
#     st.success("File uploaded")

# user_question = st.text_input(
#     "Enter Your Question : ",
#     placeholder = "Cyanobacteria can perform photosynthetsis , are they considered as plants?",
# )

# if st.button("Tell me about it", type = "primary"):
#     loader = TextLoader('text.txt')
#     index = VectorstoreIndexCreator().from_loaders([loader])
#     query = user_question
#     answer = index.query_with_sources(query)
#     st.success(answer['answer'])