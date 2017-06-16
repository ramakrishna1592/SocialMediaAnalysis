import tweepy
from tweepy import OAuthHandler
import json

consumer_key = 'HkESrNUT7EQVMZcJJBsM5Usl3'
consumer_secret = '7Rzrlp8kQt1lyK4fe8t3amgiyZ1BwfJ2IHrdHfqxehcCnnZ0dc'
access_token = '127451753-BeEHwvgpupGAathAKNNY50ONAfQ5eUn3wiOwysmP'
access_secret = 'otR8q70yPffPnqAjU6gsGHf1zTAB5NZAX2dYR8l8VwkHq'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))
