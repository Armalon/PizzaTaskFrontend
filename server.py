from flask import Flask, escape, request, url_for, render_template, make_response, g, session
# https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/#sqlite3
import sqlite3
from flask_cors import CORS

import os

# https://flask.palletsprojects.com/en/1.1.x/quickstart/
app = Flask(__name__)
CORS(app, supports_credentials=True)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

DATABASE = 'database/chat_database.db'


# getting DB instance
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

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


# Init DB
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


@app.route('/')
def home():
    # todo: Show login and passwords on a main web page for easy access

    name = request.args.get('name',
                            'World')  # this is context local https://flask.palletsprojects.com/en/1.1.x/quickstart/#context-locals
    # request.method
    # request.form
    # request.args.get
    # request.cookies.get('username')
    username = request.cookies.get('username')
    link_address = url_for('show_user_profile', username='test')
    static_link = url_for('static', filename='style.css')
    return f'Hello!, {escape(name)}. Here is the link to <a href="{link_address}">{username}</a> <br> and here is s just <a href="{static_link}">link</a>'


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        # f.save('/var/www/uploads/' + secure_filename(f.filename))


@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    return render_template('hello.html', username=username)


@app.route('/test')
def test():
    resp = make_response(render_template('just_cookies.html'))
    resp.set_cookie('username', 'the username')
    return resp


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
        error: 0,
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
        random_user = query_db('SELECT * FROM users ORDER BY RANDOM() LIMIT 1', (), True)
        if random_user != None:
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
    :return:
    {
        error: 0,
        messages: [...Message]
    }
    """
    pass


@app.route('/chat-post-message')
def chat_post_message():
    """
    Putting Message in a Chat
    :return:
    {
        error: 0,
        message: Message
    }
    """
    pass


# on app closing
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
