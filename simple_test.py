#!/usr/bin/python
# simple_test 

import logging
import BackpackLib, mybeebotte
from random import randint

mylcd = BackpackLib.lcd()
myBeebotte = mybeebotte.Mybeebotte(interval = 1, no_sensors = 1)
LENGTH = 24*30		# assuming readings are every 2 minutes, this is the last days readings

def do_it():
	mylcd.lcd_display_string("Conservatory temp.", 1)
#	temperature = myBeebotte.read()
	temperature = myBeebotte.read_group(LENGTH)
#	temperature = myBeebotte.read_stats()
	min = 30
	max = 0
	for val in temperature:
		point = val['data']
#		print point
		if point < min:
			min = point
		if point > max:
			max = point
	print 'now=',point
	print 'min=',min,' max=',max
	spoint = '{:.1f}'.format(point)
	smin = '{:.1f}'.format(min)
	smax = '{:.1f}'.format(max)
	mylcd.lcd_display_string('now='+spoint+' C', 2)
	mylcd.lcd_display_string('min='+smin+' max='+smax , 3)
#	temperature = '{:.1f}'.format(temperature)
#	print "temperature=", temperature
#	mylcd.lcd_display_string(temperature+' C', 2)
	mylcd.lcd_display_string('Stopped: simple test' , 4)

if __name__ == '__main__':
    do_it()
	