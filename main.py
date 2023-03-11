import streamlit as st
from functions import ideator
import json

def main():
    # Create a title for the chat interface
    st.title("Tara Ideator Bot")

    #initialize messages list and print opening bot message
    messages = [
        {"role": "system", "content": "You are a sassy African-American entrepeneur named Tara who helps people come up with app ideas based on their business or hobby. You ask clarifying questions about their job and hobby, then guide them towards ideas. Make it interactive and shepherd them through the process. If the user is not responding posivitely, switch to asking clarifying questions for a bit before proceeding."},
        {"role": "assistant", "content": "Hi! This is Tara. Seems like you need help coming up with an idea! Let's do this. First, what's your job?"}
        ]

    st.write(messages[1]["content"])

    # Create a text input for the user to enter their message and append it to messages
    userresponse = st.text_input("Enter your message")
    test = 1
    print(test)

    # Create a button to submit the user's message
    if st.button("Send"):
        # Generate a response to the user's message (in this example, just echoing the message)
        messages.append({"role": "user", "content": userresponse})
        messages = ideator(messages)
        test+=1
        print(test)
        # Display the response in the chat interface
        string = ""

        for message in messages[1:]:
            string = string + message["role"] + ": " + message["content"] + "\n\n"
        st.write(string)
            

if __name__ == '__main__':
    main()


    