from dotenv import load_dotenv
import tweepy
import os

load_dotenv();

class Twitter: 
    def __init__(self):
        self.twitter = tweepy.Client(
            bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
            consumer_key=os.getenv('TWITTER_API_KEY'),
            consumer_secret=os.getenv('TWITTER_API_SECRET'),
            access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET'),
            wait_on_rate_limit=True
        )
    
    def tweet(self, message):
        self.twitter.create_tweet(text=message)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("Hello World!")