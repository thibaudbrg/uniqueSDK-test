"""
Embeddings Creation Example
---------------------------

This script demonstrates how to create embeddings using the unique_sdk.
It sends an array of text to the AI model for embedding and retrieves the vector of embeddings.

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

# Define the texts to be embedded
texts = ["hello", "world"]

# Create embeddings for the provided texts
result = unique_sdk.Embeddings.create(
    user_id=user_id,
    company_id=company_id,
    texts=texts,
)

# Print the embeddings result
print("Embeddings:")
for text, embedding in zip(texts, result.embeddings):
    print(f"Text: {text}, Embedding: {embedding}")
