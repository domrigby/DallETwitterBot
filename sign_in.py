import tweepy
import random
import os

from PIL import Image

from makeImage import ImageMaker

class Tweet():

    def __init__(self,account):
        self.account = account # this object contains the account adn all its functions sucha as tweeting
        self.lyric : str

        self.generateLyric()
        self.checkLyric()

        createImage = ImageMaker(self.lyric)

        #img = Image.open(f"~/Downloads/{createImage.fileName}")

        ret = self.account.media_upload(f"home/dom/Downloads/{createImage.fileName}")

        # Attach returned media id to a tweet
        self.account.update_status(media_ids=[ret.media_id_string], status=self.lyric)


    def generateLyric(self):
        with open("Kanye_West_Lyrics.txt","r") as file:
            lines = file.readlines()
            N = len(lines)
            x = random.randint(0,N)
            self.lyric= lines[x]
            print(self.lyric)

    def checkLyric(self):
        badWords = ["nig","Nig"] # filter out strings with this in
        for word in badWords:
            if word in self.lyric:
                print("Lyric rejected")
                self.generateLyric()
        if self.lyric[0] == "[" or "\n" :
            self.generateLyric()

    def sendTweet(self):
        self.account.update_status(self.lyric)

        
def logIn():
    api_key = "QVpQ8gMTgizHl2xp3JpgIuYSo"
    api_secrets = "FAOVJk7LUjBamPFZHBZwegFUfZ2lGLNsXzd3KxD2n4cmlLIMeT"
    access_token = "1559490515183304708-Kh0ZzwRcb9U8ckAsL3Jm1UZfg0b4wO"
    access_secret = "j8fviSDwgLsOc84Q4cKOtOGgDNl20giCYWA7cX29DeNth"

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
    tweet = Tweet(account)

if __name__ == "__main__":
    global account
    account = logIn()
    main(account)