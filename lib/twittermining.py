import tweepy
api_key = "xLo0Ix5hPIm6qtNLaDoLbCOne"
api_key_secret = "Q5gzA6TzKOzh4VkmFs6odu7P8Nm6LxsLT2Sd951eiQK0DUEESu"
bearer_token = 'AAAAAAAAAAAAAAAAAAAAANhlZQEAAAAATt9qsjhnnF9bqa%2BhbgMfPmS8iL0%3DftqpOtrWXTvEZvfsT9yU1gyrKwRunLOdeL9RiyS4uWAgzrMs24'
access_token = "949282964352856066-Y55IFHsFizYxCq9GK4FwkjOOvdAxHaH"
access_token_secret = "nNtPRqbBFckn5ybdfjAAUq8ppVZmdPLNNvM0f42ydkRRn"

# Creating the authentication object
auth = tweepy.OAuthHandler(api_key, api_key_secret)
# Setting your access token and secret
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
        
    
    