velotweet
=========

A Pedal-Powered Twitter Display for [THAAT](http://www.thaat.coop/).  Using a low-powered linux system 
like a Raspberry Pi and a pico projector, a single person riding bicycle can
generate enough power to run a live updating twitter display.  The first run of
the system will be at the 2013
[HIVEX](http://www.hamiltonhive.ca/event/hivex).

Arduino Monitor
---------------
Rider performance is monitored using an arduino connected to the bike generator.
It monitors power output, speed, and distance travelled and feeds that data to
the webapp.

Webapp
------
The display code is all run using a simple python
[flask](http://flask.pocoo.org/) app.  It uses the
[twitter](https://github.com/sixohsix/twitter) module to search for tweets and
throw them up on a web page along with the rider stats from the arduino.
