#!/usr/bin/env python2
# myminbeebotte.py
# To get beebotte working....

import beebotte
import datetime

DEFAULT_INTERVAL = 2		# minutes
beebotte_api_key = "ca39e5d2f0e358fbc45ce96b2981bdae"
beebotte_secret_key = "50eaa3b5184fccbffe72da0777340b5cc33b0bb7ea5b856b1e6cd4fc86a8f66a"
beebotte_channel = "Thermometer"
beebotte_variable = "Conservatory"

class Mybeebotte():
	def __init__(self, interval = DEFAULT_INTERVAL):
		api = beebotte.BBT(beebotte_api_key, beebotte_secret_key)
		self.test_variable = beebotte.Resource(api,beebotte_channel, beebotte_variable)
		self.beebotte_interval = datetime.timedelta(minutes = interval)
		self.last_time = datetime.datetime.now()
	
	def _process(self, string):
		output = []
		data = string.split()
		data1 = float(data[2])
		output.append(data1)
		if self.no_sensors == 2:
			data2 = float(data[4])
			output.append(data2)		
		return(output) 

	def write(self, string):
	# This does not write if not enough time has passed.
		now = datetime.datetime.now()
		if ((now - self.last_time) > self.beebotte_interval):
			self.last_time = now
			data_pts = self._process(string)
			try:
				self.test_variable.write(data_pts[0])
			except:
				return(False)
		return(True)
			
	def read(self, length):
		bee = self.test_variable.read(limit = length)
		return(bee)
		
	def read_stats(self):
		bee = self.test_variable.read(limit = 10, source = 'day_stats')
		return(bee)
	
if __name__ == "__main__":
	test_write = False
	if test_write:
		print 'Writing test value to beebotte and reading it back.'
		myBeebotte = Mybeebotte(interval = 1, no_sensors = 2)	# Beware!!! Writes every minute.
		myBeebotte.write('16:15 0 10.5 1 12.5')		# Test value
		print 'Wrote'
	else:
		print 'Reading from beebotte'
		myBeebotte = Mybeebotte()
		print 'Read:', myBeebotte.read(1)
	