# this will be the main function for our project

from ast import keyword
from lib.twittermining import TwitterMining

if __name__ == "__main__": 
    test = TwitterMining(keyword="wordl", location="brookings")
    test.getTweets()