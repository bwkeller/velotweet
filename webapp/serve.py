#!/usr/bin/python
from flask import Flask, render_template, url_for
from twitter import *
app = Flask(__name__)

def grab_power():
	return 0

def grab_rpm():
	return 0

def get_tweets(hashtags):
	return 0

@app.route('/')
def render_wall():
	tags = []
	staticurls = {'css':url_for('static', filename='wall.css'),
			'thaat':url_for('static', filename='thaat.png'),
			'thinkhaus':url_for('static', filename='thinkhaus.png')}
	return render_template('wall.html', 
			static=staticurls, rpm=grab_rpm(), 
			power=grab_power(), tweets=get_tweets(tags),
			event="#HIVEX")

if __name__ == "__main__":
	app.run(debug=True)
