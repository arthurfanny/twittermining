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
        self.outfile = "data/stream_twitterarthursunforubc.json"

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
    print "Please type into how many threads do you want to do data catch from Twitter Account"
    number_process=int(raw_input())
    while (1>number_process or number_process>10):
        print "What you have entered is not a correct data type of int, Please resubmit. Thanks"
        number_process=int(raw_input())

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
    myStream.filter(track=['UBC'])

    '''
    result_queue = multiprocessing.Queue()
    listener=MyStreamListener()




    def stream(authorization,listenerax,result_queue1):
        myStream=tweepy.Stream(authorization, listenerax )
        myStream.filter(track=['python'])

    processs = []

    for n in range(4): # start 4 processes crawling for the result
        process = multiprocessing.Process(target=stream, args=[auth,listener,result_queue])
        process.start()
        processs.append(process)

    print "Waiting for result..."

    result = result_queue.get() # waits until any of the proccess have `.put()` a result

    for process in processs: # then kill them all off
        process.terminate()

    print "Got result:", result





    def streamData(data,array,authorization):
        def __init___(data, array, authorization):
            twitter_stream = Stream(authorization,MyListener(data,array))
            twitter_stream.filter(track=[array])







    process=[]
    result_queue=multiprocessing.Queue






        #process=multiprocessing.Process(target=streamData(a,b,c),args=[result_queue])
        #process.start()
        #process.join()

    #PrintStatus="Process %n has already been started"%(number_process)
    #print PrintStatus

    #result = result_queue.get() # waits until any of the proccess have `.put()` a result
#   for process in process: # then kill them all off
#        process.terminate()

    #print "Got result:", result







   # public_tweets=api.timeline()
   # for tweet in public_tweets:
   #     print tweet.text

'''