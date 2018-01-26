#!/usr/bin/env python2
# alexa_temperatures.py
# Based on....
# Memory game code for flask-ask demo as found in...
#   https://alexatutorial.com/1
# This needs....
# pip install flask-ask

import logging
import BackpackLib
import fetch_data
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)
mylcd = BackpackLib.lcd()
myData = fetch_data.Temperatures()

@ask.launch
def startup():
	print 'Startup'
	welcome_msg = render_template('welcome')
	mylcd.lcd_display_string("Alexa Temps.", 1)
	vals = myData.read()
	myData.list(vals)
	myData.lcd(vals)
	msg = render_template('done')
	return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)
	