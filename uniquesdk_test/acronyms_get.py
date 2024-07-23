"""
Acronyms Retrieval Example
---------------------------

This script demonstrates how to retrieve acronyms defined for a company using the unique_sdk.
It fetches the acronyms and prints them to the console.

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

# Retrieve the user ID and company ID from environment variables
user_id = os.getenv("USER_ID")
company_id = os.getenv("COMPANY_ID")

# Fetch the acronyms defined for the company
acronyms = unique_sdk.Acronyms.get(
    user_id=user_id,
    company_id=company_id,
)

# Print the fetched acronyms
print("Fetched Acronyms:")
for acronym in acronyms.data:
    print(f"{acronym.abbreviation}: {acronym.meaning}")
