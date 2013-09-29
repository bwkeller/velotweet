#!/usr/bin/python
from flask import Flask, render_template, url_for
import random
import os
from twitter import *
app = Flask(__name__)
MY_TWITTER_CREDS = os.path.expanduser('~/.velotweet_oauth')

def grab_power():
	return random.randint(0,500)

def grab_speed():
	return random.randint(0,50)

def grab_distance():
	return random.randint(0,500)

def munge_statuses(status):
	return {'user':status['user']['screen_name'], 'text':status['text']}

def get_tweets(hashtags):
	oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
	twitter = Twitter(auth=OAuth(oauth_token, oauth_secret,
	"pnOTHwklWj75l45HSF650g", "JyWoD0TgqE7ocSGlXNdHdKSpSmfijWS5LnikvVY"))
	tweets = twitter.search.tweets(q=hashtags, count=5, result_type='recent')
	return [munge_statuses(status) for status in tweets['statuses']]

@app.route('/')
def render_wall():
	tags = "@THAATCoop"
	staticurls = {'css':url_for('static', filename='wall.css'),
			'thaat':url_for('static', filename='thaat.png'),
			'thinkhaus':url_for('static', filename='thinkhaus.png')}
	return render_template('wall.html', 
			static=staticurls, speed=grab_speed(), 
			power=grab_power(), tweets=get_tweets(tags),
			distance=grab_distance(), event="#HIVEX")

if __name__ == "__main__":
	random.seed()
	app.run(debug=True)
