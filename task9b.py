# In your terminal, you must first set your API key:
# export OPENAI_API_KEY="sk-YOUR_REAL_KEY_HERE"

import os
from openai import OpenAI # Import the modern client

# This is the new, secure way to initialize the client
try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    exit()

if not client.api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    print("Please set it in your terminal: export OPENAI_API_KEY='your_key_here'")
    exit()

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready! Type 'quit()' to exit.")

while True:
    # 1. Get the user's message
    message = input("You: ")
    
    # 2. Check if the user wants to quit
    if message.lower() == "quit()":
        print("Goodbye!")
        break
        
    # 3. Add the user's message to the history
    messages.append({"role": "user", "content": message})
    
    try:
        # 4. Get the response from the API (using the new client syntax)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        # 5. Get the reply content (using new response attributes)
        reply = response.choices[0].message.content
        
        # 6. Add the assistant's reply to the history
        messages.append({"role": "assistant", "content": reply})
        
        print(f"\nAssistant: {reply}\n")
        
    except openai.AuthenticationError:
        print("AuthenticationError: Your API key is incorrect or invalid.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break