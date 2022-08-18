import tweepy

import datetime
import time

from tweetHandler import NewKanyeTweet, GeneralTwitter
from makeImage import ImageMaker
from imageEdditting import EditImage

        
def logIn():

    with open("signInDetails.txt","r") as file:
        keys = file.readlines()

    # Create a file of the sign in details, and then add it to the .gitignore file so that your credentials will not be pushed to GitHub

    api_key = keys[0]
    api_secrets = keys[1]
    access_token = keys[2]
    access_secret = keys[3]
    
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
    twitter = GeneralTwitter(account)
    mentionsTweets = twitter.retrieveNewMentionedTweet()
    if mentionsTweets: # empty sequences are False (another way of saying length greater than 0)
        for element in mentionsTweets:
            tweet = element[0] # this is a tweet object
            image = ImageMaker(tweet._json['text'])
            newImage = EditImage(image.tag) # im learning to use multiple files
            newImage.crop()
            twitter.sendReplyTweetwithImage(image.tag,image.text,element[1])
            image.deleteImage()
    else:
        print("No new tweets")
        pass

if __name__ == "__main__":
    global account
    account = logIn()
    while True:
        main(account)
        time.sleep(600) # check for new mentions every ten minutes
    