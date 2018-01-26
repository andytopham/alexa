#!/usr/bin/env python2
# read_temperature. Reads latest temperature from beebotte cloud and writes to lcd.
#  

import logging
import BackpackLib, Mybeebotte
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)
mylcd = BackpackLib.lcd()

@ask.launch
def new_game():
	welcome_msg = render_template('welcome')
	mylcd.lcd_display_string("Conservatory temperature", 1)
	myBeebotte = Mybeebotte(interval = 1, no_sensors = 1)
	temperature = myBeebotte.read(1)
	print "temperature=", temperature
	mylcd.lcd_display_string(temperature, 2)
	return question(welcome_msg)

@ask.intent("YesIntent")
def next_round():
	numbers = [randint(0, 9) for _ in range(3)]
	mylcd.lcd_display_string("Numbers", 2)
	mylcd.lcd_display_string(str(numbers[0])+' '+str(numbers[1])+' '+str(numbers[2]), 3)
	round_msg = render_template('round', numbers=numbers)
	session.attributes['numbers'] = numbers[::-1]  # reverse
	return question(round_msg)

@ask.intent("AnswerIntent", convert={'first': int, 'second': int, 'third': int})
def answer(first, second, third):
	mylcd.lcd_display_string(str(first)+' '+str(second)+' '+str(third), 4)
	winning_numbers = session.attributes['numbers']
	if [first, second, third] == winning_numbers:
		msg = render_template('win')
	else:
		msg = render_template('lose')
	return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)
	