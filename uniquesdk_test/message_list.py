"""
Message Listing Example
------------------------

This script demonstrates how to list messages for a single chat using the unique_sdk.
It retrieves and prints all messages in the specified chat.

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

# List messages for the specified chat
messages = unique_sdk.Message.list(
    user_id=user_id,
    company_id=company_id,
    chatId=chat_id,
)

# Print the fetched messages
print("Messages in Chat:")
for message in messages.data:
    print(f"{message.role}: {message.text}")
