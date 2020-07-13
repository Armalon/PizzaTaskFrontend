# MyFirstPythonServer

A basic implementation for my first python server which is gonna be a chat with an authorization.
All in one script server using Flask as a web server and SQLite3 as a Data Base.

Python version 3.7+ is required. 
As well as the [virtualenv module](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
 

## How to start

1. Create and activate a python environment

`python3 -m venv .env && source .env/bin/activate`

(For later deactivation run)

`deactivate`

2. Install all the project dependencies

`pip install -r requirements.txt`

3. Init db by running the following script

`python init_db.py` 

4. Start the App as a service using flask

`env FLASK_APP=server.py flask run`