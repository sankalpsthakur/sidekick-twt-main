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

# Dictionary of dates and tweets
tweet_dict = {
    '22-Jun-23': 'Thinking about scaling vs growth. Growth is not always scaling, but scaling always involves growth. A company can grow but may not necessarily scale. #growth #scaling',
    '23-Jun-23': 'The power of technology is limitless, but it is the human mind that wields it. Tech without the right thought leadership is just a tool without a hand. #technology #AI',
    # ... Fill in the rest of your tweets here ...
}

# Function to post tweet based on the date
def job_tweet():
    today = time.strftime('%d-%b-%y')  # get today's date
    tweet_text = tweet_dict.get(today)
    if tweet_text:
        create_tweet(consumer_key, consumer_secret, access_token, access_token_secret, tweet_text)

# Schedule job to run every day at 12:00
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
