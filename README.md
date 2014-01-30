# ScoutBase

ScoutBase is a webb application written in python for keeping track of
scouting infromation at FIRST Tech Challenge competitions.  The main goals
of the project were developing a way keep track of a unified set of
quanitifiable data sets when scouting other teams at competition.  The project
is currently still in development and does not have extensive documentation.
For any feedback or questions shoot me an email at <figitaki96@yahoo.com>.

## Dependancies

ScoutBase requires Python 2.7, to ensure this is available on your machine execute
the command '$ python -v'.  Also, the (web.py)[http://webpy.org] is required.
It is simple to install with the easy install feature:

	$ sudo easy_install web.py

A Postgre SQL database is also necessary, see the web.py documentation for more
information on how to set one up.

## Running

After fulfilling the dependancies all that is left is getting the latest code
and running the main.py script.  By default the app runs on port 8080, but it
is easy to change this by passing in a runtime argument to the program as shown
below.

	// get the latest code
	$ git clone http://git.com/figitaki/scoutbase.git
	$ cd scoutbase

	// run the webapp
	$ python main.py
	http://0.0.0.0:8080/

	// or run on a diffrent port
	$ python main.py 1234
	http://0.0.0.0:1234/

If you have any problems or would like to suggest improvements just submit a ticket to
the repo or shoot me an email. Thanks!
