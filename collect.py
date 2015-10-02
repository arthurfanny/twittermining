import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import threading
import argparse
import string
import json
import multiprocessing

consumer_key='e04NKQICzPWqO7rPx0MFdt7pv'
consumer_secret='zBcKhBa2USjqN5EZxKrcHR9OM3ubkyyyEQBfRvttKTmGlJBMjR'
access_token='3535129333-oUtL0wppTmsLMObzsQW4bvlcZZN73t1EcccE6nG'
access_secret='BrvawMYlz1O1HighzEZxeHIKoYIe8Mm52VbL0JCDxTJw4'

class MyStreamListener(tweepy.StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self):
        #query_fname = format_filename("twitter")
        self.outfile = "data/stream_collection.json"

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        print(status)
        return True

if __name__ == '__main__':
    print "Welcome to the Twitter Parser InfoVis Program\n"
    print "Now Downloading Twitter Info.... Press Ctrl+C to stop collection process"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
    myStream.filter(track=['python'])
