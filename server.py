# All in one Simple Chat server using Flask as a web server and SQLite3 as DB
# Made for educational purposes


# IMPORTS SECTION>
import os
import time
import stat

from config import Config

# https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/#sqlite3
from flask import Flask, escape, request, url_for, render_template, make_response, g, session
from flask_cors import CORS

# https://docs.python.org/3/library/sqlite3.html
import sqlite3
# <IMPORTS SECTION


# INIT APP>
# A link to a SQLite DB file
DATABASE = 'database/chat_database.db'

# Setting up a Flask server
app = Flask(__name__)
# Using a CORS module for cross domain requests between Front and Back
CORS(app, supports_credentials=True)

# Applying the config
app.config.from_object(Config)

# On app closing
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
# <INIT APP


# ROUTING>
@app.route('/')
def home():
    result = {
        'error': 0
    }
    return result


@app.route('/login')
def login():
    """
    Checking if user is authorized and authorizing if not (as a random user)
    req.args: {
        # login: String,
        # pass: String
    }
    :return:
    {
        user: User,
        error: 0,  # 2 - DB error
    }
    """

    result = {
        'error': 0,
        'user': None
    }
    if 'user_id' in session:
        result['user'] = {
            'id': session['user_id'],
            'name': session['user_name'],
        }
    else:
        try:
            random_user = query_db('SELECT * FROM users ORDER BY RANDOM() LIMIT 1', (), True)
            # todo: Return a Row object and turn it into a predefined model
        except sqlite3.Error as ex:
            result['error'] = 2
            # or raise further maybe
            return result

        if random_user is not None:
            result['user'] = random_user
            session['user_id'] = random_user['id']
            session['user_name'] = random_user['name']
        else:
            result['error'] = 1
    return result


@app.route('/logout')
def logout():
    """
    Logging user out
    :return:
    {
        error: 0,
    }
    """
    session.pop('user_id', None)
    session.pop('user_name', None)
    return {
        'error': 0
    }


@app.route('/mychats')
def mychats():
    """
    Show Chats where I can write
    :return:
    {
        error: 0,
        chats: [...Chat]
    }
    """
    result = {
        'error': 0,
        'chats': []
    }
    if 'user_id' in session:
        chats_rows = query_db('SELECT * FROM chats WHERE user1_id = ? OR user2_id = ?', [session['user_id'], session['user_id']])
        result['chats'] = chats_rows
    # for chat in query_db('select * from chats'):
    #     print(chat['name'])
    return result


@app.route('/chat-messages')
def chat_messages():
    """
    Show all Messages in a Chat
    req.args: {
        chat_id
    }
    :return:
    {
        error: 0,
        messages: [...Message]
    }
    """
    result = {
        'error': 1,
        'messages': []
    }

    if request.args.get('chat_id') is not None:
        messages = query_db('SELECT * FROM chat_messages WHERE chat_id = ?', [request.args.get('chat_id')])
        result['error'] = 0
        result['messages'] = messages

    return result


@app.route('/chat-post-message')
def chat_post_message():
    """
    Putting Message in a Chat
    req.args: {
        chat_id,
        text
    }
    :return:
    {
        error: 0,
        message: Message
    }
    """
    result = {
        'error': 1,  # Not authorized
        'message': None
    }

    if 'user_id' in session \
            and request.args.get('chat_id') is not None \
            and request.args.get('text') is not None:
        message = {
            'text': request.args.get('text'),
            'user_id': session['user_id'],
            'datetime': round(time.time()),
            'chat_id': request.args.get('chat_id')
        }
        inserted_id = insert_db(
            'INSERT INTO chat_messages (text, user_id, datetime, chat_id) VALUES (:text, :user_id, :datetime, :chat_id)',
            message
        )
        message['id'] = inserted_id
        result['message'] = message
    return result
# <ROUTING


# HELPERS>
# getting DB instance
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

    # db.set_trace_callback(print)

    def make_dicts(cursor, row):
        return dict((cursor.description[idx][0], value)
                    for idx, value in enumerate(row))
    db.row_factory = make_dicts

    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def insert_db(query, args=()):
    cur = get_db().cursor()
    cur.execute(query, args)
    get_db().commit()
    return cur.lastrowid
# <HELPERS


# Init DB method for external usage
# Usage:
# >>> from server import init_db
# >>> init_db()
def init_db():
    if os.path.exists(DATABASE):
        os.remove(DATABASE)

    with app.app_context():
        db = get_db()
        with app.open_resource('chat_schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

    os.chmod(
        DATABASE,
        stat.S_IRUSR |
        stat.S_IWUSR |
        stat.S_IRGRP |
        stat.S_IWGRP |
        stat.S_IROTH |
        stat.S_IWOTH
    )
