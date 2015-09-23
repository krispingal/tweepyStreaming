#! /usr/bin/env python3

# Create a listener for Twitter Stream API 1.1
import csv
from tweepy.streaming import StreamListener
import time
import sys

class SListenerCsv(StreamListener):
	
	def __init__(self, api=None, fprefix = 'streamer'):
		self.api = api or API()
		self.counter = 0;
		self.fprefix = fprefix;
		self.writer = csv.writer(open('../streaming_data/'  + fprefix + '-' + time.strftime('%Y%m%d-%H:%m:%S') + '.csv', 'wb+'))
		#create column headers 
		self.writer.writerow(('created_at', 'text', 'coordinates', 'user.time_zone'))
	
	'''write to a particular file 20k lines/tweet status'''
	def on_status(self, status):
		#print str(status.created_at), status.text, status.coordinates, status.author.time_zone
		self.writer.writerow([str(status.created_at), status.text.encode('utf-8'), status.coordinates, status.author.time_zone])
		
		self.counter += 1
		if self.counter > 20000:
			#self.writer.close()
			self.writer = csv.writer(open('../streaming_data/'  + self.fprefix + '-' + time.strftime('%Y%m%d-%H:%m:%S') + '.csv', 'wb+'))
			self.writer.writerow(('created_at', 'text', 'coordinates', 'user.time_zone'))
			#reset counter to 0
			self.counter = 0
	
	def on_error(self, status_code):
		print >>sys.stderr, 'Encountered error with status code:', status_code
		#don't stop continue listening to the stream
		return True
			
