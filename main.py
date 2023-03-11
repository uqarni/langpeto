#generate openai response; returns messages with openai response
def ideator_gpt(messages):
  import openai
  import os
  key = "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"
  openai.api_key = key

  work = "doctor"
  hobby = "fishing"


  result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= messages
  )
  response = result["choices"][0]["message"]["content"]
  response = {
    "role": "assistant", 
    "content": response
  }
  messages.append(response)

  return messages


#prompt user with botresponse in terminal and ask for an input. returns messages with human response
def terminaltalker(messages):

  botresponse = messages[-1]["content"]
  userresponse = input(botresponse+"\n")
  messages.append(
  {
    "role": "user",
    "content": userresponse
  }
  )
  return messages


def terminalbot():
    #initialize message
    messages = [
          {"role": "system", "content": "You are a sassy back entrepeneur named Tara who helps people come up with app ideas based on their business or hobby. You ask clarifying questions about their job and hobby, then guide them towards ideas. Make it interactive and shepherd them through the process. If the user is not responding posivitely, switch to asking clarifying questions for a bit before proceeding."},
          {"role": "assistant", "content": "Hi! This is Tara. Seems like you need help coming up with an idea! Let's do this. First, what's your job?"}
          ]
    while True:
       messages = terminaltalker(messages)
       if messages[-1]["content"] == "exit()":
          break
       ideator_gpt(messages)




      
  