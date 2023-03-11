
# [
#           {"role": "system", "content": "You are a bot that comes up with 10 mobile app business ideas based on either the user's job, hobby, or both"},
#           {"role": "user", "content": "I work as a " + work + " and my main hobby is "+hobby+". Start your response with a comment about how cool my job and hobby are."},
#     ]

#call chatgpt with messages and openai API key
def ideator_gpt(messages, key):
  import openai
  import os

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


test = [
           {"role": "system", "content": "You are a sassy back entrepeneur named Tara who helps people come up with app ideas based on their business or hobby. You often ask clarifying questions to guide them to ideas instead of just giving them ideas."},
           {"role": "user", "content": "Hi, my job is an architect and I like to go fishing."},
     ]
call = ideator_gpt(messages = test, key = "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")
print(call[-1])

