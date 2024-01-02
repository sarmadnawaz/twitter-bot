from dotenv import load_dotenv
from twitter import Twitter
from llm import LLM
import schedule
import json
import time

load_dotenv()

file_path = "prompts.json"

with open(file_path, 'r') as file:
    prompts = json.load(file)
    file.close()

counter = 0
max_prompts = len(prompts)

def run():
    global counter
    try:
        if counter == max_prompts:
            counter = 0

        prompt = prompts[counter].get("prompt")
        twitter = Twitter()
        response = LLM().generate(f"{prompt} \n Instructions: tweet shouldn't be longer than 280 characters.")
        print(f"Tweeting: {response}")
        twitter.tweet(response)

        counter += 1
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Run every 1 hour
    schedule.every(1).hour.do(run)
    while True:
        schedule.run_pending()
        time.sleep(1)