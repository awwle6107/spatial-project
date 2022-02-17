import tweepy
from pathlib import Path

consumer_key_path = '../../twitter_key/comsumer_key.txt'
consumer_secret_path = '../../twitter_key/consumer_secret.txt'
access_token_path = '../../twitter_key/access_token.txt'
access_token_secret_path = '../../twitter_key/access_token_secret.txt'
bearer_token_path = '../../twitter_key/bearer_token.txt'

consumer_key = Path(consumer_key_path).read_text()
consumer_secret = Path(consumer_secret_path).read_text()
access_token = Path(access_token_path).read_text()
access_token_secret = Path(access_token_secret_path).read_text()
bearer_token = Path(bearer_token_path).read_text()

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret``
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

class TwitterMining: 
    def __init__(self, keyword, location):
        self.keyword = keyword
        self.location = location
    
    def getTweets(self):
        # Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
        public_tweets = api.home_timeline()
        # foreach through all tweets pulled
        for tweet in public_tweets:
        # printing the text stored inside the tweet object
            print (tweet.text)
            break        
        
    
    