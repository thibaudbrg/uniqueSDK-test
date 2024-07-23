import os
import time
import requests
import tiktoken
import unique_sdk
from dotenv import load_dotenv
from joke_of_the_day_prompts import (
    JOKE_OF_THE_DAY_SYSTEM_PROMPT,
    JOKE_OF_THE_DAY_TRIGGER_PROMPT,
    get_random_joke
)

load_dotenv()
unique_sdk.api_key = os.getenv("API_KEY")
unique_sdk.app_id = os.getenv("APP_ID")
unique_sdk.api_base = os.getenv("API_BASE")

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
maxToken = 3000

def jokeOfTheDay(event, logger):
    userId = event["userId"]
    companyId = event["companyId"]
    chatId = event["payload"]["chatId"]
    userMessage = event["payload"]["userMessage"]["text"]
    userMessageId = event["payload"]["userMessage"]["id"]
    assistantMessageId = event["payload"]["assistantMessage"]["id"]

    try:
        LanguageModel = event["payload"]["configurations"]["languageModel"]
    except KeyError:
        LanguageModel = "AZURE_GPT_4_TURBO_1106"

    # Extract relevant names (Step 2)
    unique_sdk.Message.modify(
        user_id=userId,
        company_id=companyId,
        id=assistantMessageId,
        chatId=chatId,
        text="Starting joke app..."
    )

    unique_sdk.Content.search(
        user_id=userId,
        company_id=companyId,
        where={
            "OR": [
                {"title": {"contains": "42"}},
                {"key": {"contains": "42"}}
            ]
        },
        chatId=chatId,
    )

    unique_sdk.Message.modify(
        user_id=userId,
        company_id=companyId,
        id=assistantMessageId,
        chatId=chatId,
        text="Now getting input from https://api.namefake.com/..."
    )

    time.sleep(2)
    person = get_fake_person(logger)

    if not person:
        unique_sdk.Message.modify(
            user_id=userId,
            company_id=companyId,
            id=assistantMessageId,
            chatId=chatId,
            text="Sorry, I couldn't fetch a fake person to create a joke."
        )
        return "Error", 500

    unique_sdk.Message.modify(
        user_id=userId,
        company_id=companyId,
        id=assistantMessageId,
        chatId=chatId,
        text=f"Making a joke with that name {person['name']}..."
    )

    history = unique_sdk.Message.list(
        user_id=userId,
        company_id=companyId,
        chatId=chatId,
    )

    # Process history for GPT
    history_gpt = []
    for i in history["data"][:-1]:
        history_gpt.append(
            {
                "role": "user" if i["role"] != "USER" else "assistant",
                "content": i["text"]
            }
        )

    sys_prompt = JOKE_OF_THE_DAY_SYSTEM_PROMPT
    usr_prompt = JOKE_OF_THE_DAY_TRIGGER_PROMPT.format(USERMESSAGE=userMessage, PERSON=person["name"])
    msg = [
        {"role": "system", "content": sys_prompt},
        *history_gpt,
        {"role": "user", "content": usr_prompt}
    ]

    unique_sdk.Integrated.chat_stream_completion(
        user_id=userId,
        company_id=companyId,
        assistantMessageId=assistantMessageId,
        message=msg,
        userMessageId=userMessageId,
        chatId=chatId,
    )

    return "OK", 200

def get_fake_person(logger):
    response = requests.get("https://api.namefake.com/")
    if response.status_code == 200:
        person = response.json()
        logger.info(f"Fake person data retrieved: {person}")
        return person
    else:
        logger.error("Error occurred while retrieving fake person data.")
        return None
