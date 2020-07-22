from app import app, session

import sqlite3

from app.models import User


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


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
            random_user = User.load_random_user()
        # todo: Catch a sqlalchemy error instead
        except sqlite3.Error as ex:
            result['error'] = 2
            # or raise further maybe
            return result

        if random_user is not None:
            result['user'] = {
                'id': random_user.id,
                'name': random_user.username
            }
            session['user_id'] = random_user.id
            session['user_name'] = random_user.username
        else:
            result['error'] = 1
    return result

