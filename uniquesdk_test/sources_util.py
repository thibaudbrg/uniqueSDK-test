"""
Sources Utility Example
------------------------

This script demonstrates how to use the sources utility functions from unique_sdk.
It includes merging, sorting, and post-processing of search results.

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

# Perform a search to get search context
search_results = unique_sdk.Search.create(
    user_id=user_id,
    company_id=company_id,
    chatId=chat_id,
    searchString="Who is Harry P?",
    searchType="COMBINED",
    limit=30,
    chatOnly=False,
)

search_context = search_results.data

# Merge sources
merged_sources = unique_sdk.util.sources.merge_sources(search_context)
print("Merged Sources:")
print(merged_sources)

# Sort sources
sorted_sources = unique_sdk.util.sources.sort_sources(search_context)
print("Sorted Sources:")
print(sorted_sources)

# Post-process sources
sample_text = "This is a reference [source0]"
post_processed_text = unique_sdk.util.sources.post_process_sources(sample_text)
print("Post-Processed Text:")
print(post_processed_text)
