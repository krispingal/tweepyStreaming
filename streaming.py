#! /usr/bin/env python

#import time
import tweepy
import sys
import streamListener
import logging


#logger = logging.getLogger(__name__)
#OAuth part

#provide your app's auth details
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

def main():
	logging.basicConfig(filename='streaming.log', filemode='w', level=logging.DEBUG)
	track = ['a', 'the', 'i', 'you']
	#track = ['refugeeswelcome', 'refugeecrisis']	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	listen = streamListener.SListenerCsv(api, 'generic')
	
	stream = tweepy.Stream(auth, listen)
	
	logging.info("Streaming started ...")
	
	try:
		stream.filter(languages=["en"], track = track, async=True)
	except tweepy.TweepError as ex:
		print ex.message[0]['code']
		print ex.args[0][0]['code']
		stream.disconnect()
		logger.critical('Encountered fatal exception', exc_info=True)
	
if __name__ == '__main__':
	main()
