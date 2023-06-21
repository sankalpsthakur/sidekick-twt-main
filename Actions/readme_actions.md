To run these functions, you can call them like this:

# Fetch tokens
resource_owner_key, resource_owner_secret = fetch_tokens(consumer_key, consumer_secret)

# Get authorization URL and verifier
verifier = get_authorization_url(consumer_key, consumer_secret, resource_owner_key, resource_owner_secret)

# Get access tokens
access_token, access_token_secret = get_access_tokens(consumer_key, consumer_secret, resource_owner_key, resource_owner_secret, verifier)

# Like a tweet
like_tweet(consumer_key, consumer_secret, access_token, access_token_secret, user_id, tweet_id)
