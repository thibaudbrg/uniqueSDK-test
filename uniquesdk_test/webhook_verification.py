"""
Webhook Verification Example
-----------------------------

This script demonstrates how to verify webhook signatures using the unique_sdk.
It sets up a Flask application to handle and verify incoming webhooks.

Setup:
1. Ensure you have a valid API key and App ID.
2. Make sure the .env file is correctly set up with your credentials.
3. Install Flask if not already installed (`pip install flask`).

Dependencies:
- python-dotenv
- unique_sdk
- flask
"""

import os
from http import HTTPStatus
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import unique_sdk

# Load environment variables from .env file
load_dotenv()

# Set API key and App ID for unique_sdk
unique_sdk.api_key = os.getenv("UNIQUE_SDK_API_KEY")
unique_sdk.app_id = os.getenv("UNIQUE_SDK_APP_ID")

# Retrieve the endpoint secret from environment variables
endpoint_secret = os.getenv("ENDPOINT_SECRET")

# Initialize Flask application
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    """
    Handles incoming webhooks and verifies their signatures.

    Returns:
        Response: JSON response indicating success or failure.
    """
    event = None
    payload = request.data

    sig_header = request.headers.get("X-Unique-Signature")
    timestamp = request.headers.get("X-Unique-Created-At")

    if not sig_header or not timestamp:
        print("⚠️  Webhook signature or timestamp headers missing.")
        return jsonify(success=False), HTTPStatus.BAD_REQUEST

    try:
        event = unique_sdk.Webhook.construct_event(
            payload, sig_header, timestamp, endpoint_secret
        )
    except unique_sdk.SignatureVerificationError as e:
        print(f"⚠️  Webhook signature verification failed: {e}")
        return jsonify(success=False), HTTPStatus.BAD_REQUEST

    # Process the verified event
    print(f"Received event: {event}")

    return jsonify(success=True), HTTPStatus.OK

if __name__ == "__main__":
    app.run(port=5000)
