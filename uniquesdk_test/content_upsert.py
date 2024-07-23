"""
Content Upsert Example
-----------------------

This script demonstrates how to upsert (upload or update) content using the unique_sdk.
It uploads a file and updates its metadata.

Setup:
1. Ensure you have a valid API key and App ID.
2. Make sure the .env file is correctly set up with your credentials.

Dependencies:
- python-dotenv
- unique_sdk
- requests
"""

import os
import requests
from dotenv import load_dotenv
import unique_sdk

# Load environment variables from .env file
load_dotenv()

# Set API key and App ID for unique_sdk
unique_sdk.api_key = os.getenv("UNIQUE_SDK_API_KEY")
unique_sdk.app_id = os.getenv("UNIQUE_SDK_APP_ID")

# Retrieve the user ID, company ID, and scope ID from environment variables
user_id = os.getenv("USER_ID")
company_id = os.getenv("COMPANY_ID")
file_path = "path/to/your/file.pdf"  # Change this to the actual file path
displayed_filename = "test.pdf"
mime_type = "application/pdf"
scope_id = "your_scope_id"  # Change this to the actual scope ID

def upload_file(user_id, company_id, path_to_file, displayed_filename, mime_type, scope_id):
    """
    Uploads a file and updates its metadata in the unique_sdk.

    Args:
        user_id (str): The user ID.
        company_id (str): The company ID.
        path_to_file (str): The path to the file to be uploaded.
        displayed_filename (str): The filename to be displayed.
        mime_type (str): The MIME type of the file.
        scope_id (str): The scope ID for the content.

    Returns:
        created_content: The created content metadata.
    """
    size = os.path.getsize(path_to_file)
    created_content = unique_sdk.Content.upsert(
        user_id=user_id,
        company_id=company_id,
        input={
            "key": displayed_filename,
            "title": displayed_filename,
            "mimeType": mime_type,
        },
        scopeId=scope_id,
    )

    upload_url = created_content.writeUrl

    # Upload the file to the provided URL
    with open(path_to_file, "rb") as file:
        requests.put(
            upload_url,
            data=file,
            headers={
                "X-Ms-Blob-Content-Type": mime_type,
                "X-Ms-Blob-Type": "BlockBlob",
            },
        )

    unique_sdk.Content.upsert(
        user_id=user_id,
        company_id=company_id,
        input={
            "key": displayed_filename,
            "title": displayed_filename,
            "mimeType": mime_type,
            "byteSize": size,
        },
        scopeId=scope_id,
        readUrl=created_content.readUrl,
    )

    return created_content

# Upload the file and print the result
created_content = upload_file(user_id, company_id, file_path, displayed_filename, mime_type, scope_id)
print(f"Uploaded content: Title - {created_content.title}, Key - {created_content.key}")
