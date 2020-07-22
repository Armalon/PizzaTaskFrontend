from app import app, session, request

import sqlite3

from app.models import User, Product


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


@app.route('/menu')
def menu():
    filters = request.args
    # filtering out all not valid keys
    filters = {k: v for (k, v) in filters.items() if k in {'type', 'base', 'crust'}}

    products = Product.get_by_filters(filters)
    products = [v.to_dict() for v in products]

    return {
        'products': products
    }

