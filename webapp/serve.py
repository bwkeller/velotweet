#!/usr/bin/python
from flask import Flask, render_template, url_for
from datetime import timedelta, datetime
import random #DEMO
import RPi.GPI as GPIO
import os
from twitter import *
app = Flask(__name__)
rotations = 0l
RES = 10 #The number of rotations to smooth the time measurement over
t_per_RES = 0 #The time to make the last RES rotations (in hours)
lasttime = datetime(1988, 8, 29)
PIN = 14 #Use GPIO pin 14 by default.
CIRCUMFRENCE = 2e-3
MY_TWITTER_CREDS = os.path.expanduser('~/.velotweet_oauth')

def count_rotation():
	rotations += 1
	if rotations % RES == 0:
		d = datetime.now()-lasttime
		lasttime = datetime.now()
		t_per_RES = d.total_seconds()/3600.

def grab_power():
	'''
	Return the current power output of the cyclist in watts.
	@rtype:			number
	@return:		power output in W
	'''
	return RESISTANCE*grab_speed()*0.2778 #Convert km/h -> m/s

def grab_speed():
	'''
	Return the current speed of the cyclist in km/h.
	@rtype:			number
	@return:		speed in km/h
	'''
	return RES*rotations/t_per_RES

def grab_distance():
	'''
	Return the cumulative distance rode in km.
	@rtype:			number
	@return:		distance in km
	'''
	return rotations*CIRCUMFRENCE

def munge_statuses(status):
	'''
	Convert a tweet object into a dict containing the username and 
	the text of the tweet.
	@type status:	Tweet object
	@param status:	The tweet to process
	@rtype:			dict
	@return:		username & text dictionary
	'''
	return {'user':status['user']['screen_name'], 'text':status['text']}

def get_tweets(tags):
	'''
	Search twitter for tweets that include any values in the list hashtags.
	@type tags:		string
	@param tags:	The hashtags to search for, separated by spaces
	@rtype:			dict
	@return:		username & text dictionary
	'''
	oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
	twitter = Twitter(auth=OAuth(oauth_token, oauth_secret,
	"pnOTHwklWj75l45HSF650g", "JyWoD0TgqE7ocSGlXNdHdKSpSmfijWS5LnikvVY"))
	tweets = twitter.search.tweets(q=tags, count=5, result_type='recent')
	return [munge_statuses(status) for status in tweets['statuses']]

@app.route('/')
def render_wall():
	hashtags = "@THAATCoop" #Probably should read this from a config file...
	staticurls = {'css':url_for('static', filename='wall.css'),
			'thaat':url_for('static', filename='thaat.png'),
			'thinkhaus':url_for('static', filename='thinkhaus.png')}
	return render_template('wall.html', 
			static=staticurls, speed=grab_speed(), 
			power=grab_power(), tweets=get_tweets(hashtags),
			distance=grab_distance(), event="#HIVEX")

if __name__ == "__main__":
	#Start the timing
	lasttime = datetime.now()
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(PIN, GPIO.IN) 
	#Intialize the callback function
	GPIO.add_event_detect(PIN, GPIO.RISING)
	GPIO.add_event_callback(PIN, count_rotation)
	random.seed() #DEMO needs random data for now...
	app.run(debug=True)
