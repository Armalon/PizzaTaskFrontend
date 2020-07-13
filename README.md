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

## How to test

It's an backend API service which response in the JSON format. So it works better with a Frontent part.

But you can do queries just using your browser. For example 

For logging in you can open in a browser the following link

`http://localhost:5000/login`

The system will authorize you as a random user from DB (Anthony or Yan) and remember your session.

To see your chats list please open the following. Must be logged in first!

`http://localhost:5000/mychats`

To see chat messages for a Chat #1 open

`http://localhost:5000/chat-messages?chat_id=1`

To add message to the Chat #1 do

`http://localhost:5000/chat-post-message?chat_id=1&text=Some%20text%20here`

ETC