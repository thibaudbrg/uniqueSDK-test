"""
Search String Create Example
----------------------------

This script demonstrates how to create a search string using the unique_sdk.
It transforms a user message into an ideal search string for use in the Search.create API method.

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

# Define the user message
user_message = "Was ist der Sinn des Lebens, des Universums und des ganzen Rests?"

# Create a search string from the user message
search_string = unique_sdk.SearchString.create(
    user_id=user_id,
    company_id=company_id,
    prompt=user_message,
    chat_id=chat_id,
)

# Print the search string result
print("Search String:")
print(search_string.result)
