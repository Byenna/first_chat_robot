import os
import openai
import config

 
openai.api_key = config.FIRST_CHAT_BOT



 

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "i struggle to write a hello world program in python"
    },
    {
      "role": "assistant",
      "content": "you are code reflectionGPT. you reflect on everything i write to help me learn and improve"
    },
   ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

 

print(response)