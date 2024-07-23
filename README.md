# UniqueSDK Test Project

This project demonstrates the usage of the `unique_sdk` for various functionalities provided by Unique FinanceGPT. Each script in this project illustrates a different feature of the SDK.

## Setup

### Prerequisites

- Python 3.11 or later
- [Poetry](https://python-poetry.org/) for dependency management
- [Flask](https://flask.palletsprojects.com/) for webhook verification example

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/uniquesdktest.git
    cd uniquesdktest
    ```

2. Set up your virtual environment and install dependencies:

    ```bash
    poetry install
    ```

3. Create a `.env` file in the root directory and populate it with your credentials. You can use the provided `.env.example` as a template:

    ```bash
    cp .env.example .env
    # Edit .env and add your actual values
    ```

### Environment Variables

Your `.env` file should look something like this:

```env
UNIQUE_SDK_API_KEY=your_api_key_here
UNIQUE_SDK_APP_ID=your_app_id_here
USER_ID=your_user_id_here
COMPANY_ID=your_company_id_here
CHAT_ID=your_chat_id_here
ASSISTANT_ID=your_assistant_id_here
ENDPOINT_SECRET=your_endpoint_secret_here
```

### Running the Scripts 

Activate your virtual environment:


```bash
poetry shell
```

Then you can run each script individually:


```bash
python uniquesdk_test/acronyms_get.py
python uniquesdk_test/chat_completions.py
python uniquesdk_test/chat_history_util.py
python uniquesdk_test/content_search.py
python uniquesdk_test/content_upsert.py
python uniquesdk_test/embeddings_create.py
python uniquesdk_test/file_io.py
python uniquesdk_test/message_create.py
python uniquesdk_test/message_list.py
python uniquesdk_test/message_retrieve.py
python uniquesdk_test/message_modify.py
python uniquesdk_test/message_delete.py
python uniquesdk_test/chat_stream_completion.py
python uniquesdk_test/search_create.py
python uniquesdk_test/search_string_create.py
python uniquesdk_test/short_term_memory.py
python uniquesdk_test/sources_util.py
python uniquesdk_test/uniqueql_query.py
python uniquesdk_test/webhook_verification.py
```

## File Descriptions 
 
- `acronyms_get.py`:
Demonstrates how to retrieve acronyms defined for a company using the `unique_sdk`.
 
- `chat_completions.py`:
Shows how to create a chat completion using the AI model supported by Unique FinanceGPT.
 
- `chat_history_util.py`:
Illustrates how to load chat history and convert it into an injectable string format.
 
- `content_search.py`:
Demonstrates how to search for content based on specific criteria.
 
- `content_upsert.py`:
Shows how to upsert (upload or update) content and update its metadata.
 
- `embeddings_create.py`:
Illustrates how to create embeddings for an array of text.
 
- `file_io.py`:
Demonstrates file operations such as downloading and uploading files to the knowledge-base.
 
- `message_create.py`:
Shows how to create a new message in a chat.
 
- `message_list.py`:
Demonstrates how to list messages for a specific chat.
 
- `message_retrieve.py`:
Demonstrates how to retrieve a single chat message.
 
- `message_modify.py`:
Demonstrates how to modify an existing chat message.
 
- `message_delete.py`:
Demonstrates how to delete a chat message.
 
- `chat_stream_completion.py`:
Demonstrates how to stream chat completion to the chat frontend.
 
- `search_create.py`:
Illustrates how to perform a search query on the Unique FinanceGPT Knowledge database.
 
- `search_string_create.py`:
Demonstrates how to create a search string from a user message for more effective searching.
 
- `short_term_memory.py`:
Shows how to use the short term memory functionality to save and retrieve data between chat interactions.
 
- `sources_util.py`:
Demonstrates how to use the sources utility functions, including merging, sorting, and post-processing of search results.
 
- `uniqueql_query.py`:
Shows how to perform a search with detailed metadata filtering using UniqueQL.
 
- `webhook_verification.py`:
Sets up a Flask application to handle and verify incoming webhooks, ensuring their signatures are valid.

## License 
This project is licensed under the MIT License - see the LICENSE  file for details.
## Acknowledgements
This project uses the [Unique FinanceGPT](https://github.com/Unique-AG/ai/tree/main/unique_sdk) API for various functionalities.
