#!/usr/bin/python
from flask import Flask
from twitter import *
app = Flask(__name__)

def grab_power():
	return 0

def grab_rpm():
	return 0

def get_tweets(hashtags):
	return 0

@app.route('/')
def hello_world():
	return 'Hello World!'

if __name__ == "__main__":
	app.run()
