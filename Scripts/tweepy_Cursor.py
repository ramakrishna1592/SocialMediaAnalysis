import tweepy_oAuth

# for status in tweepy.Cursor(api.home_timeline).items(10):
#     process_or_store(status._json)
#
# for friend in tweepy.Cursor(api.friends).items(20):
#     process_or_store(friend._json)

for tweet in tweepy_oAuth.tweepy.Cursor(tweepy_oAuth.api.user_timeline).items(20):
    tweepy_oAuth.process_or_store(tweet._json)
