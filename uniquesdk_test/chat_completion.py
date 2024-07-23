"""
Chat Completion Example
-----------------------

This script demonstrates how to create a chat completion using the unique_sdk.
It sends a prompt to an AI model supported by Unique FinanceGPT and prints the result.

Setup:
1. Ensure you have a valid API key and App ID.
2. Make sure the .env file is correctly set up with your credentials.

Dependencies:
- python-dotenv
- unique_sdk
"""

import os
from dotenv import load_dotenv
import unique_sdk

# Load environment variables from .env file
load_dotenv()

# Set API key and App ID for unique_sdk
unique_sdk.api_key = os.getenv("UNIQUE_SDK_API_KEY")
unique_sdk.app_id = os.getenv("UNIQUE_SDK_APP_ID")

# Retrieve the company ID from environment variables
company_id = os.getenv("COMPANY_ID")

# Define the messages for the chat completion
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"},
]

# Create a chat completion
chat_completion = unique_sdk.ChatCompletion.create(
    company_id=company_id,
    model="AZURE_GPT_35_TURBO",  # Define the model to be used
    messages=messages,
)

# Print the result of the chat completion
print("Chat Completion Result:")
for choice in chat_completion.choices:
    print(choice.message["content"])
