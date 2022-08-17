from cgitb import text
import tweepy
import tweepy
import random
import os

from PIL import Image

from makeImage import ImageMaker
from imageEdditting import EditImage

import pickle

class GeneralTwitter():

    def __init__(self,account):
        self.account = account

        self.accountName = self.account

        self.mentionsList = []
        self.storageName = "previous_mentions.pkl"
        self.mentionsText = []

    def sendTweet(self,tweet):
        self.account.update_status(NewTweet)

    def getMentions(self):
        self.mentions = self.account.mentions_timeline()

        #for mention in self.mentions:
            #self.mentionsList.append(mention._json['text'])
        
    def retrieveMentionedTweet(self):
        for status in self.mentions:
            try:
                tweet = self.account.get_status(status._json['in_reply_to_status_id'])
                tweetText = tweet._json['text']
            except :
                pass
            self.mentionsText.append(tweetText)

        return self.mentionsText


class NewKanyeTweet(GeneralTwitter):

    def __init__(self,account):
        super().__init__(account)

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

        createImage.deleteImage() # save space


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

