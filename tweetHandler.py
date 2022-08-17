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

        self.storageName = "previous_mentions.pkl"
        self.taggedTweets = []

    def sendTweet(self,tweet):
        self.account.update_status(tweet)
            
        
    def retrieveMentionedTweet(self):
        self.mentions = self.account.mentions_timeline()
        self.taggedTweets = []

        with open(self.storageName, 'rb') as pickle_file:
            alreadyDone = pickle.load(pickle_file)

        for status in self.mentions:
            try:
                tweet = self.account.get_status(status._json['in_reply_to_status_id']) # object for tweet being replied to
                tweet_ID = status._json['id'] # id off tweet with tag
                if tweet_ID not in alreadyDone: # check we havent already replied to this tweet
                    self.taggedTweets.append([tweet,status._json["id"]]) # return an array of the tweet object to make an image, along with the id to reply to
                    alreadyDone.append(tweet_ID)
            except :
                pass

        with open(self.storageName,"wb") as f:
            pickle.dump(alreadyDone,f)
            print(alreadyDone)

        return self.taggedTweets


    def sendReplyTweetwithImage(self,imageLocation,status,id):

        print(imageLocation)

        ret = self.account.media_upload(imageLocation)

        # Attach returned media id to a tweet
        self.account.update_status(media_ids=[ret.media_id_string], status=status, in_reply_to_status_id = id , auto_populate_reply_metadata=True)


class NewKanyeTweet(GeneralTwitter):

    def __init__(self,account):
        super().__init__(account)

        self.account = account # this object contains the account adn all its functions sucha as tweeting
        self.lyric : str

        self.generateLyric()

        createImage = ImageMaker(self.lyric)

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

