# Bot Setup Guide

This Twitter bot is designed to periodically post tweets on a Twitter account using the OpenAI language model (LLM). Follow these steps to set it up on your local machine for personal use.

## Prerequisites

- Python 3.x installed on your system
- Twitter Developer Account
- OpenAI API Key

## Installation Steps

# 1. Clone the Repository

Clone the repository containing the Twitter bot code:

```bash
git clone https://github.com/your_username/twitter-bot.git
cd twitter-bot
```

# 2. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

# 3. Set Up Environment Variables

Create a .env file in the root directory of the project and add the following environment variables:

```plaintext
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
OPENAI_API_KEY=your_openai_api_key
```
Replace your_twitter_* and your_openai_api_key with your actual Twitter API keys and OpenAI API key.

# 4. Run the Bot

Execute the bot by running the following command:

```bash
python bot.py
```

The bot will start posting tweets at regular intervals according to the specified schedule.

## Usage

Once the bot is running, it will automatically post tweets periodically based on the specified schedule.
