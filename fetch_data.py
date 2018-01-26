#!/usr/bin/env python2
# fetch_data.py

import BackpackLib, myminbeebotte

LENGTH = 24*30		# assuming readings are every 2 minutes, this is the last days readings

class Temperatures():
	def __init__(self):
		self.mylcd = BackpackLib.lcd()
		self.myBeebotte = myminbeebotte.Mybeebotte()
	
	def read(self):
		readings = self.myBeebotte.read(LENGTH)
		min = 30
		max = 0
		for val in readings:
			point = val['data']
			if point < min:
				min = point
			if point > max:
				max = point
		now = readings[0]['data']
		spoint = '{:.1f}'.format(now)
		smin = '{:.1f}'.format(min)
		smax = '{:.1f}'.format(max)
		return(spoint, smin, smax)

	def list(self, val):
		print 'now=', val[0]
		print 'min=',val[1],' max=',val[2]
		
	def lcd(self, val):
		self.mylcd.lcd_display_string("Conservatory temp.  ", 1)
		self.mylcd.lcd_display_string('now='+val[0]+' C   ', 2)
		self.mylcd.lcd_display_string('min='+val[1]+' max='+val[2]+'  ' , 3)
		self.mylcd.lcd_display_string('Stopped: fetch_data ' , 4) # any excess chars wrap to first line!
	
if __name__ == '__main__':
	myTemp = Temperatures()
	values = myTemp.read()
	myTemp.list(values)
	myTemp.lcd(values)
	
	