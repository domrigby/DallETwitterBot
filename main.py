import tweepy

import datetime
import time

from tweetHandler import NewKanyeTweet, GeneralTwitter

        
def logIn():

    api_key = "N1u5g4S1fsOACYRiubkhgarCR"
    api_secrets = "qFEsASRNsaPwMSANhahUaZWAEHy8XSlB5xF6FwFCQ7X7aDJkBw"
    access_token = "1559490515183304708-Zl4bXJM4SiK6dzH4H6HswvjaTyHPkE"
    access_secret = "FPREilxkO4OxlaI25cpiQrsbjW1wmmdQoGE6eWAj2gMJG"

    # bearer token : AAAAAAAAAAAAAAAAAAAAABMbgAEAAAAAIFpx3hZMabSHOWOAteIfAg9cWWY%3DUdGSjBvQyp2RBeg1owlU4VOd7n4vSDEpfM3vzVsqKPWuK6MMGN
    
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(api_key,api_secrets)
    auth.set_access_token(access_token,access_secret)
    
    api = tweepy.API(auth)
    
    try:
        api.verify_credentials()
        print('Successful Authentication')
    except Exception as e:
        print(e)
        print('Failed authentication')

    return api

def main(account):
    check = GeneralTwitter(account)
    check.getMentions()
    check.retrieveMentionedTweet()
    twitter = NewKanyeTweet(account)

if __name__ == "__main__":
    global account
    account = logIn()
    while True:
        main(account)
        time.sleep(500)
    