from app import app, session, request, db

import sqlite3

from app.models import User, Product, ProductOrder, Order, OrderStatus

from config import SERVICE_INFO

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
            'phone': session['user_phone'],
            'address': session['user_address'],
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
                'name': random_user.username,
                'phone': random_user.phone,
                'address': random_user.address,
            }
            session['user_id'] = random_user.id
            session['user_name'] = random_user.username
            session['user_phone'] = random_user.phone
            session['user_address'] = random_user.address
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
    session.pop('user_phone', None)
    session.pop('user_address', None)
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
        'error': 0,
        'products': products
    }


@app.route('/make_order', methods=['POST'])
def make_order():
    result = {
        'error': 1,
        'order': None
    }

    if request.get_json().get('order') is None\
            or request.get_json().get('name') is None\
            or request.get_json().get('phone') is None\
            or request.get_json().get('address') is None:
        return result

    if 'user_id' in session and session['user_name'] == request.get_json().get('name'):
        pass
    else:
        # Registering a new user using provided name and address
        user = User.load_user_by_phone(request.get_json().get('phone'))
        if user is None:
            user = User(username=request.get_json().get('name'), address=request.get_json().get('address'), phone=request.get_json().get('phone'))
            db.session.add(user)
            db.session.commit()

        session['user_id'] = user.id
        session['user_name'] = user.username
        session['user_phone'] = user.phone
        session['user_address'] = user.address

    user_result = {
        'id': session['user_id'],
        'name': session['user_name'],
        'phone': session['user_phone'],
        'address': session['user_address']
    }
    result['user'] = user_result

    o = Order(user_id=user_result['id'],
              username=request.get_json().get('name'),
              address=request.get_json().get('address'),
              phone=request.get_json().get('phone'))

    o.total_price = SERVICE_INFO['delivery_price']

    order_products = request.get_json().get('order')
    for order_product in order_products:
        p = Product.query.get(order_product['id'])
        if p is None or order_product['quantity'] is None:
            result.error = 2
            return result

        o.total_price += order_product['quantity'] * p.price

        po = ProductOrder(product=p, quantity=order_product['quantity'], order=o)
        db.session.add(po)

    o.status = OrderStatus.ORDERED
    db.session.add(o)
    db.session.commit()

    result['error'] = 0
    result['order'] = o.to_dict()
    return result


@app.route('/my_orders')
def my_orders():
    result = {
        'error': 1,
        'orders_list': None
    }
    if 'user_id' not in session:
        return result

    result['error'] = 0
    result['orders_list'] = [order.to_dict() for order in Order.get_my_orders(session['user_id'])]

    return result


@app.route('/service_info')
def service_info():
    return {
        'info': SERVICE_INFO,
        'error': 0
    }

