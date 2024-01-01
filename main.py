from dotenv import load_dotenv
from twitter import Twitter
from llm import LLM
import schedule
import time

load_dotenv();

def run():
    try:
        twitter = Twitter()
        response = LLM().generate("Tell an interesting fun fact. Make sure the return text is less than 280 characters.")
        twitter.tweet(response)
    except Exception as e:
        print(f"Error: {e}");

if __name__ == "__main__":
    # Run every 1 hour
    schedule.every(1).hour.do(run)
    while True:
        schedule.run_pending()
        time.sleep(1)
