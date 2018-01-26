# alexa code
Code for being a slave to an alexa skill.

## Alexa skill

### To get it to run in the simulator on the developer website, need to use US English.
 - Skill = show temperatures
 
### To get it to run on an Echo, need to use UK English.
 - Skill = my temperatures

## For RPi being a slave
flask-ask
- templates.yaml - the strings to be spoken. This file used by flask-ask.
- alexa_temperatures - main routine to run on rpi to provide remote alexa functionality.
  - fetch_data.py - local version of above for testing.
    - myminbeebotte.py - streamlined version of mybeebotte.py
    BackpackLib.py


## Another version
flask-ask
- templates.yaml - the strings to be spoken. This file used by flask-ask.
- read_temperature.py - a big flask-ask app that returns the temperatures. work in progress.
  - simple_test.py - an older and fuller app to return temps.
    - mybeebotte.py - old version.
    - BackpackLib.py
 
## Running help
start_ngrok.sh - run this in another terminal once alexa_temperatures is running.
 
