import os
import json
from requests_oauthlib import OAuth1Session



def like_tweet(consumer_key, consumer_secret, access_token, access_token_secret, id, tweet_id):
    # Making the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )
    response = oauth.post(
        "https://api.twitter.com/2/users/{}/likes".format(id), json={"tweet_id": tweet_id}
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))

def unlike_tweet(consumer_key, consumer_secret, access_token, access_token_secret, id, tweet_id):
    # Making the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )
    response = oauth.delete(
        "https://api.twitter.com/2/users/{}/likes/{}".format(id, tweet_id)
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))

def retweet(consumer_key, consumer_secret, access_token, access_token_secret, id, tweet_id):
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)
    response = oauth.post("https://api.twitter.com/2/users/{}/retweets".format(id), json={"tweet_id": tweet_id})

    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
        
    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))

def undo_retweet(consumer_key, consumer_secret, access_token, access_token_secret, id, source_tweet_id):
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)
    response = oauth.delete("https://api.twitter.com/2/users/{}/retweets/{}".format(id, source_tweet_id))

    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
        
    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))

def create_tweet(consumer_key, consumer_secret, access_token, access_token_secret, text):
    payload = {"text": text}
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)
    response = oauth.post("https://api.twitter.com/2/tweets", json=payload)

    if response.status_code != 201:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
        
    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))

def delete_tweet(consumer_key, consumer_secret, access_token, access_token_secret, id):
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)
    response = oauth.delete("https://api.twitter.com/2/tweets/{}".format(id))

    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
        
    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))
