"""
File IO Example
---------------

This script demonstrates how to download and upload files using the unique_sdk.
It covers file operations such as downloading content and uploading files to the knowledge-base.

Setup:
1. Ensure you have a valid API key and App ID.
2. Make sure the .env file is correctly set up with your credentials.

Dependencies:
- python-dotenv
- unique_sdk
- requests
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

# Define the file path for downloading and uploading
file_path = "/tmp/downloaded_file.pdf"
displayed_filename = "uploaded_file.pdf"
mime_type = "application/pdf"
scope_id = "your_scope_id"  # Change this to the actual scope ID

def download_content(company_id, user_id, content_id, filename):
    """
    Downloads a file from the unique_sdk knowledge-base.

    Args:
        company_id (str): The company ID.
        user_id (str): The user ID.
        content_id (str): The content ID to download.
        filename (str): The filename to save the downloaded content.

    Returns:
        None
    """
    pdf_file = unique_sdk.util.file_io.download_content(
        company_id=company_id,
        user_id=user_id,
        content_id=content_id,
        filename=filename,
        chat_id=None  # If specified, it downloads it from the chat
    )
    print(f"Downloaded content saved as {filename}")

def upload_file(company_id, user_id, path_to_file, displayed_filename, mime_type, upload_scope):
    """
    Uploads a file to the unique_sdk knowledge-base.

    Args:
        company_id (str): The company ID.
        user_id (str): The user ID.
        path_to_file (str): The path to the file to be uploaded.
        displayed_filename (str): The filename to be displayed.
        mime_type (str): The MIME type of the file.
        upload_scope (str): The scope ID for the content.

    Returns:
        created_content: The created content metadata.
    """
    created_content = unique_sdk.util.file_io.upload_file(
        company_id=company_id,
        user_id=user_id,
        path_to_file=path_to_file,
        displayed_filename=displayed_filename,
        mimeType=mime_type,
        uploadScope=upload_scope,
        chat_id=None,
    )
    print(f"Uploaded content: Title - {created_content.title}, Key - {created_content.key}")

# Download a file
content_id = "your_content_id"  # Change this to the actual content ID
download_content(company_id, user_id, content_id, file_path)

# Upload a file
upload_file(company_id, user_id, file_path, displayed_filename, mime_type, scope_id)
