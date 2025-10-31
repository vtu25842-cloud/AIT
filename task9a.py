# The "pip install openai" command should be run in your terminal,
# not inside the Python script.

# In your Terminal:
# pip install openai

import openai
import os # Import os to securely access environment variables

# --- SECURITY WARNING ---
# DO NOT paste your API key directly into the code.
# The key you posted is now public and MUST be revoked.

# SECURE METHOD:
# 1. Set an environment variable in your terminal:
#    export OPENAI_API_KEY="sk-YOUR_REAL_KEY_HERE"
# 2. Access it in your code like this:
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if the key was loaded
if openai.api_key is None:
    print("Error: OPENAI_API_KEY environment variable not set.")
    # You might want to exit or raise an error here
else:
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Give me 3 ideas that I could build using OpenAI APIs"}
            ]
        )
        print(completion.choices[0].message.content)

    except openai.error.AuthenticationError:
        print("AuthenticationError: Your API key is incorrect or has been revoked.")
    except Exception as e:
        print(f"An error occurred: {e}")