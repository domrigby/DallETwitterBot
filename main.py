import tweepy
import random
import os

from PIL import Image

from makeImage import ImageMaker
from imageEdditting import EditImage

class Tweet():

    def __init__(self,account):
        self.account = account # this object contains the account adn all its functions sucha as tweeting
        self.lyric : str

        self.generateLyric()

        createImage = ImageMaker(self.lyric)

        #img = Image.open(f"~/Downloads/{createImage.fileName}")

        image = EditImage(createImage.tag) # im learning to use multiple files
        image.crop()

        ret = self.account.media_upload(createImage.tag)

        # Attach returned media id to a tweet
        self.account.update_status(media_ids=[ret.media_id_string], status=self.lyric)


    def generateLyric(self):
        with open("Kanye_West_Lyrics.txt","r") as file:
            lines = file.readlines()
            N = len(lines)
            x = random.randint(0,N)
            self.lyric= lines[x]
            print(self.lyric)
            self.checkLyric()

    def checkLyric(self):
        badWords = ["nig","Nig","bitch","Bitch"] # filter out strings with this in
        for word in badWords:
            if word in self.lyric:
                print("Lyric rejected")
                self.generateLyric()
        if self.lyric[0] == "[" or len(self.lyric) < 10:
            self.generateLyric()


    def sendTweet(self):
        self.account.update_status(self.lyric)

        
def logIn():
    # log in here

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