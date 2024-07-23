"""
Search Create Example
----------------------

This script demonstrates how to perform a search using the unique_sdk.
It performs a search query on the Unique FinanceGPT Knowledge database and prints the results.

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

# Perform a search on the Unique FinanceGPT Knowledge database
search_results = unique_sdk.Search.create(
    user_id=user_id,
    company_id=company_id,
    chatId=chat_id,
    searchString="What is the meaning of life, the universe and everything?",
    searchType="COMBINED",  # Options are VECTOR, COMBINED
    chatOnly=False,
    scopeIds=["your_scope_id"],  # Replace with actual scope IDs
    limit=20,
    page=1,
)

# Print the search results
print("Search Results:")
for result in search_results.data:
    print(f"Title: {result.title}, URL: {result.url}")
