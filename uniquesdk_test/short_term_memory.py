"""
Short Term Memory Example
--------------------------

This script demonstrates how to use the short term memory functionality of the unique_sdk.
It saves data between chat interactions and retrieves it for use in the next interaction.

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

# Define the memory name and data to be saved
memory_name = "example_memory"
data_to_save = "This is some example data to save."

# Save data to short term memory
short_term_memory = unique_sdk.ShortTermMemory.create(
    user_id=user_id,
    company_id=company_id,
    data=data_to_save,
    chatId=chat_id,
    memoryName=memory_name,
)

# Print the result of saving data
print("Saved Short Term Memory:")
print(short_term_memory)

# Retrieve the latest short term memory
retrieved_memory = unique_sdk.ShortTermMemory.find_latest(
    user_id=user_id,
    company_id=company_id,
    chatId=chat_id,
    memoryName=memory_name,
)

# Print the retrieved memory
print("Retrieved Short Term Memory:")
print(retrieved_memory)
