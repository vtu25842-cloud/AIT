# In your terminal, you MUST set your API key first:
# export OPENAI_API_KEY="sk-YOUR_REAL_KEY_HERE"

import openai
import gradio as gr # Renamed for standard practice
import os

# --- Secure API Key Setup ---
# Load the API key from environment variables
# NEVER paste your key directly into the code.
try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Check if the key was actually loaded
    if not client.api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please run: export OPENAI_API_KEY='your_key_here'")
        exit()
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    exit()

# --- System Message ---
# This defines the bot's permanent personality.
system_message = {
    "role": "system",
    "content": "You are a financial expert that specializes in real estate investment and negotiation"
}

def CustomChatGPT(message, history):
    """
    This function is called by Gradio for each new user message.
    'message' is the new message from the user.
    'history' is the past conversation (a list of [user, assistant] pairs).
    """
    
    # Start building the list of messages for the API
    messages_for_api = [system_message]
    
    # Add the past conversation (history)
    for user_msg, bot_msg in history:
        messages_for_api.append({"role": "user", "content": user_msg})
        messages_for_api.append({"role": "assistant", "content": bot_msg})
        
    # Add the user's new message
    messages_for_api.append({"role": "user", "content": message})
    
    try:
        # --- Call the API (Modern v1.0+ Syntax) ---
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages_for_api
        )
        
        # Get the reply
        reply = response.choices[0].message.content
        return reply
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"Sorry, an error occurred: {e}"

# --- Gradio ChatInterface ---
# This is the modern, correct way to build a chatbot in Gradio.
# It automatically handles the chat history (session state).
demo = gr.ChatInterface(
    fn=CustomChatGPT,
    title="Intelligent Chatbot (Real Estate Expert)",
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Ask me about real estate", container=False, scale=7),
    submit_btn="Send",
    retry_btn=None,
    undo_btn=None,
    clear_btn="Clear Conversation"
)

# Launch the app
demo.launch(share=True)