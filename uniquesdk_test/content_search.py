"""
Content Search Example
-----------------------

This script demonstrates how to search for content using the unique_sdk.
It performs a search query to retrieve content based on specific criteria.

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

# Perform a content search with specific criteria
contents = unique_sdk.Content.search(
    user_id=user_id,
    company_id=company_id,
    where={
        "OR": [
            {"title": {"contains": "42"}},
            {"key": {"contains": "42"}}
        ]
    },
    chatId=chat_id
)

# Print the fetched content titles
print("Fetched Content:")
for content in contents.data:
    print(f"Title: {content.title}, Key: {content.key}")
