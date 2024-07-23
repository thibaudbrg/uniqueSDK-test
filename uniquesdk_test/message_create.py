"""
Message Creation Example
-------------------------

This script demonstrates how to create a new message in a chat using the unique_sdk.
It sends a message to the specified chat and prints the result.

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

# Retrieve the user ID, company ID, chat ID, and assistant ID from environment variables
user_id = os.getenv("USER_ID")
company_id = os.getenv("COMPANY_ID")
chat_id = os.getenv("CHAT_ID")
assistant_id = os.getenv("ASSISTANT_ID")

# Create a new message in the specified chat
message = unique_sdk.Message.create(
    user_id=user_id,
    company_id=company_id,
    chatId=chat_id,
    assistantId=assistant_id,
    text="Hello, how can I assist you today?",
    role="ASSISTANT",
)

# Print the result of the message creation
print(f"Created Message: {message.text}")
