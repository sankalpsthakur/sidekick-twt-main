import os
import random
import schedule
import time
from Actions.manage_actions import (
    retweet,
    create_tweet,
    like_tweet
)
from Actions.auth import (
    fetch_tokens,
    get_authorization_url,
    get_access_tokens,
)

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")


resource_owner_key, resource_owner_secret = fetch_tokens(consumer_key, consumer_secret)
verifier = get_authorization_url(consumer_key, consumer_secret, resource_owner_key, resource_owner_secret)
access_token, access_token_secret = get_access_tokens(consumer_key, consumer_secret, resource_owner_key, resource_owner_secret, verifier)

# you need to implement this function to get tweets from @sankalpsthakur
def get_past_tweets():
    # Implement function to fetch past tweets
    pass

# schedule retweet
def job_retweet():
    past_tweets = get_past_tweets()
    tweet_to_retweet = random.choice(past_tweets)
    retweet(consumer_key, consumer_secret, access_token, access_token_secret, id, tweet_to_retweet['id'])

# schedule.every().day.at("15:00").do(job_retweet)

# schedule tweet
tweet_dict = {
    # fill your tweets here
    # 'day1': 'Hello, Twitter!',
    # 'day2': 'Another day, another tweet.',
    # ...
}

def job_tweet():
    today = time.strftime('%A').lower()  # get today's day of week
    tweet_text = tweet_dict.get(today)
    if tweet_text:
        create_tweet(consumer_key, consumer_secret, access_token, access_token_secret, tweet_text)

schedule.every().day.at("12:00").do(job_tweet)

# schedule like tweets
def job_like():
    # Here we should get the most recent tweets from the timeline
    # And then call `like_tweet` function on them
    # However, this depends on Twitter's API and how it's implemented
    pass

# schedule.every().day.at("17:00").do(job_like)

while True:
    schedule.run_pending()
    time.sleep(1)
