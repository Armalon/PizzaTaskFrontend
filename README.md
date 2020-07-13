# MyFirstPythonServer

A basic implementation for my first python server which is gonna be a chat with an authorization.
All in one script server using Flask as a web server and SQLite3 as a Data Base.

Python version 3.7+ is required

## How to start

1. Activate a python environment

`source server-env/bin/activate`

(For deactivation run)

`deactivate`

2. Start the App as a service using flask

`env FLASK_APP=server.py flask run`