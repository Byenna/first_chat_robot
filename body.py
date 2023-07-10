# import os
# import openai
# import config
# import flet as ft

# openai.api_key = config.FIRST_CHAT_BOT

# print("Welcome to the interactive chat! You can type 'quit' to exit.")

# while True:
#     user_input = input("User: ")

#     if user_input.lower() == "quit":
#         break

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "user",
#                 "content": user_input
#             }
#         ],
#         temperature=0.7,
#         max_tokens=100,
#         top_p=1.0,
#         frequency_penalty=0.0,
#         presence_penalty=0.0
#     )

#     assistant_response = response.choices[0].message['content']
#     print("Assistant:", assistant_response)