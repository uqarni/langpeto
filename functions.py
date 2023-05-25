#generate openai response; returns messages with openai response
def ideator(messages):
  import openai
  import os
  key = os.environ.get("OPENAI_API_KEY")
  openai.api_key = key

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
#change this from input function to streamlit function
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

#starts terminal conversation. Respond with exit() to exit. 
def terminalbot():
    import redis
    redis_host = os.environ.get("REDIS_1_HOST")
    redis_port = 25061
    redis_password = os.environ.get("REDIS_1_PASSWORD")
    rd = redis.Redis(host=redis_host, port=redis_port, password=redis_password, ssl=True, ssl_ca_certs="/etc/ssl/certs/ca-certificates.crt")

    system_prompt = rd.get("matej@closersintoleaders.com-systemprompt-01").decode('utf-8')
    
    #initialize message
    messages = [
          {"role": "system", "content": system_prompt},
          {"role": "assistant", "content": "Hey [NAME] - Pat here from Cole Gordon's Remote Closing Academy. I saw you were potentially considering getting into remote closing. Are you still looking into doing that? Let me know, I might have a few resources I can send over or help point you in the right direction. If you don't want me to text you, just reply 'stop' and I'll cease all communication moving forward :)"}          ]
    while True:
       messages = terminaltalker(messages)
       if messages[-1]["content"] == "exit()":
          break
       ideator(messages)
