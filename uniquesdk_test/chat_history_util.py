"""
Chat History Utility Example
----------------------------

This script demonstrates how to use the chat history utility functions from unique_sdk.
It loads the chat history and converts it into an injectable string format.

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

# Retrieve the user ID, company ID, and chat ID from environment variables
user_id = os.getenv("USER_ID")
company_id = os.getenv("COMPANY_ID")
chat_id = os.getenv("CHAT_ID")

# Load the chat history
history = unique_sdk.utils.chat_history.load_history(
    user_id=user_id,
    company_id=company_id,
    chatId=chat_id,
    maxTokens=1000,  # Maximum tokens for the model used
    percentOfMaxTokens=0.15,  # Percentage of max tokens for the history
    maxMessages=4,  # Maximum number of messages to include in the history
)

# Convert the chat history to an injectable string
chat_history_string, chat_context_token_length = unique_sdk.utils.chat_history.convert_chat_history_to_injectable_string(
    history
)

# Print the chat history and token length
print("Chat History String:")
print(chat_history_string)
print(f"Chat Context Token Length: {chat_context_token_length}")
