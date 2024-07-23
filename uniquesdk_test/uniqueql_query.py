"""
UniqueQL Query Example
-----------------------

This script demonstrates how to use UniqueQL for metadata filtering in unique_sdk.
It performs a search with detailed metadata filtering.

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
from unique_sdk.util.uniqueql import UQLOperator, UQLCombinator

# Load environment variables from .env file
load_dotenv()

# Set API key and App ID for unique_sdk
unique_sdk.api_key = os.getenv("UNIQUE_SDK_API_KEY")
unique_sdk.app_id = os.getenv("UNIQUE_SDK_APP_ID")

# Retrieve the user ID, company ID, and chat ID from environment variables
user_id = os.getenv("USER_ID")
company_id = os.getenv("COMPANY_ID")
chat_id = os.getenv("CHAT_ID")

# Define a metadata filter using UniqueQL
metadata_filter = {
    "path": ['diet', '*'],
    "operator": UQLOperator.NESTED,
    "value": {
        UQLCombinator.OR: [
            {
                UQLCombinator.OR: [
                    {
                        "path": ['food'],
                        "operator": UQLOperator.EQUALS,
                        "value": "meat",
                    },
                    {
                        "path": ['food'],
                        "operator": UQLOperator.EQUALS,
                        "value": 'vegis',
                    },
                ],
            },
            {
                "path": ['likes'],
                "operator": UQLOperator.EQUALS,
                "value": True,
            },
        ],
    },
}

# Perform a search with metadata filtering
search_results = unique_sdk.Search.create(
    user_id=user_id,
    company_id=company_id,
    chatId=chat_id,
    searchString="Search for specific diet preferences",
    searchType="COMBINED",
    metaDataFilter=metadata_filter,
)

# Print the search results
print("Search Results with Metadata Filtering:")
for result in search_results.data:
    print(f"Title: {result.title}, URL: {result.url}")
