"""
Retrieve a single chat message using unique_sdk.
"""

import os
from dotenv import load_dotenv
import unique_sdk

# Load environment variables from .env file
load_dotenv()

# Set API key and App ID for unique_sdk
unique_sdk.api_key = os.getenv("UNIQUE_SDK_API_KEY")
unique_sdk.app_id = os.getenv("UNIQUE_SDK_APP_ID")

# Retrieve user ID, company ID, chat ID, and message ID from environment variables
user_id = os.getenv("USER_ID")
company_id = os.getenv("COMPANY_ID")
chat_id = os.getenv("CHAT_ID")
message_id = os.getenv("MESSAGE_ID")

# Get a single chat message
message = unique_sdk.Message.retrieve(
    user_id=user_id,
    company_id=company_id,
    id=message_id,
    chatId=chat_id,
)

print(message)
