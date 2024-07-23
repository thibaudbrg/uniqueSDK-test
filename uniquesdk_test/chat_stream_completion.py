"""
Stream chat completion to the chat frontend using unique_sdk.
"""

import os
from dotenv import load_dotenv
import unique_sdk

# Load environment variables from .env file
load_dotenv()

# Set API key and App ID for unique_sdk
unique_sdk.api_key = os.getenv("UNIQUE_SDK_API_KEY")
unique_sdk.app_id = os.getenv("UNIQUE_SDK_APP_ID")

# Retrieve necessary IDs from environment variables
user_id = os.getenv("USER_ID")
company_id = os.getenv("COMPANY_ID")
chat_id = os.getenv("CHAT_ID")
assistant_message_id = os.getenv("ASSISTANT_MESSAGE_ID")
user_message_id = os.getenv("USER_MESSAGE_ID")

# Stream chat completion
unique_sdk.Integrated.chat_stream_completion(
    user_id=user_id,
    company_id=company_id,
    assistantMessageId=assistant_message_id,
    userMessageId=user_message_id,
    messages=[
        {
            "role": "system",
            "content": "be friendly and helpful"
        },
        {
            "role": "user",
            "content": "hello"
        }
    ],
    chatId=chat_id,
    searchContext=[
        {
            "id": "ref_qavsg0dcl5cbfwm1fvgogrvo",
            "chunkId": "0",
            "key": "some reference.pdf : 8,9,10,11",
            "sequenceNumber": 1,
            "url": "unique://content/cont_p8n339trfsf99oc9f36rn4wf"
        }
    ],  # optional
    debugInfo={
        "hello": "test"
    },  # optional
    startText="I want to tell you about: ",  # optional
    model="AZURE_GPT_4_32K_0613",  # optional
    timeout=8000,  # optional in ms
    temperature=0.3,  # optional
)

print("Stream completed.")
