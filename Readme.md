# 3News API Using LangChain and OpenAI

3News is an API that returns the latest news articles based on the type of news requested, powered by large language models (LLMs) and LangChain. The API supports five different news categories: **local**, **international**, **business**, **tech**, and **sports**. It processes requests dynamically based on the type of news and location (if needed).

## Features

- **Five types of news**: Local, International, Business, Tech, and Sports.
- **Location support**: Location can be provided for specific news categories like local and business.
- **LLM-powered**: Leverages LangChain and OpenAI's GPT-4 for generating and selecting relevant news based on the input.

## News Types Supported
- **local**: News based on a provided location (e.g., city, country).
- **international**: News on global events.
- **business**: Business-related news tailored to a specific region or globally.
- **tech**: News related to technology trends.
- **sports**: Sports-related news, optionally filtered by location.

**Note**: The input is **not case-sensitive**, but it is **spelling-sensitive**. Make sure to use the exact names for the news types (e.g., `local`, not `Local`).

## Setup Instructions

### 1. Create a Python Virtual Environment

To ensure an isolated environment, you need to create a virtual environment for the project:

#### For Windows:
```bash
python -m venv venv
```

#### For macOS/Linux:
```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

#### For Windows:
```bash
.\venv\Scripts\activate
```

#### For macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies

Use the `requirements.txt` file to install all the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory of the project to store necessary environment variables:

```env
GROQ_API_KEY={not used in the current configuration}
LANGCHAIN_API_KEY={your_langchain_api_key}
LANGCHAIN_TRACING_V2=true
OPENAI_API_KEY={your_openai_api_key}
```

Replace `{your_langchain_api_key}` and `{your_openai_api_key}` with the actual API keys.

### 5. Run the API

Start the API server by running:

```bash
python main.py
```

This will start the server on `http://localhost:8000`.

### 6. Test the API

Send a `POST` request to `http://localhost:8000/news` with a JSON body like:

```json
{
    "news_type": "local",
    "location": "Berlin, Germany"
}
```

You can use tools like [Postman](https://www.postman.com/) or `curl` to test the API.

### Example cURL request:

```bash
curl -X 'POST' \
  'http://localhost:8000/news' \
  -H 'Content-Type: application/json' \
  -d '{
  "news_type": "local",
  "location": "Berlin, Germany"
}'
```

### 7. Response Format

The API returns a JSON array with the following keys:
- **name**: The title of the news article.
- **content**: A summary of the article.
- **source**: The news source or publisher.
- **date**: The date the article was published.

Example response:

```json
[
    {
        "name": "Nova Scotia Government Announces New Environmental Policy",
        "content": "The government of Nova Scotia has introduced a new environmental policy aimed at reducing carbon emissions by 50% over the next decade.",
        "source": "CBC News",
        "date": "2023-09-28"
    },
    {
        "name": "Major Traffic Revisions in Halifax Starting Next Week",
        "content": "Starting next Monday, major traffic revisions will be implemented in downtown Halifax.",
        "source": "Halifax Chronicle-Herald",
        "date": "2023-09-28"
    },
    {
        "name": "Nova Scotia Schools to Implement New STEM Curriculum",
        "content": "Nova Scotia's Department of Education has announced the rollout of a new STEM-focused curriculum in all public schools.",
        "source": "Global News",
        "date": "2023-09-28"
    }
]
```

## Environment Variables

The following environment variables are required and should be set in the `.env` file:

- **GROQ_API_KEY**: Not currently in use with this configuration.
- **LANGCHAIN_API_KEY**: Your LangChain API key.
- **LANGCHAIN_TRACING_V2**: Set to `true` to enable tracing.
- **OPENAI_API_KEY**: Your OpenAI API key.

### Example `.env` file:

```env
GROQ_API_KEY={not used in the current configuration}
LANGCHAIN_API_KEY={your_langchain_api_key}
LANGCHAIN_TRACING_V2=true
OPENAI_API_KEY={your_openai_api_key}
```

## Troubleshooting

If you run into issues, ensure that:

- The environment variables in the `.env` file are correctly set.
- Both API keys (LangChain and OpenAI) are valid and correctly placed in the `.env` file.
- All dependencies from `requirements.txt` are installed correctly.

For more troubleshooting tips related to LangChain, check out their [documentation](https://python.langchain.com/docs/troubleshooting/errors/INVALID_PROMPT_INPUT).

---

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
