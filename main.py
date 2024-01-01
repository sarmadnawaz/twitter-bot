from dotenv import load_dotenv
from twitter import Twitter
from llm import LLM

load_dotenv();

if __name__ == "__main__":
    try:
        twitter = Twitter()
        response = LLM().generate("How is the weather today in London?")
        twitter.tweet(response)
        print(response);
    except Exception as e:
        print(e);

