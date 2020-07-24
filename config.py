import os
import random
import string

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret key for Session
    # byte encoded random string of length 16
    # Notice: All sessions will be dropped on web server restart
    SECRET_KEY = os.environ.get('SECRET_KEY') or str.encode(''.join(
        random.choice(string.ascii_lowercase) for i in range(16)
    ))

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

SERVICE_INFO = {
    'delivery_price': 4,
    'usd_to_eur_multiplier': 1.16,
}

ORDER_STATUS_EXPIRATION = {
    'CONFIRMED_AFTER': 1 * 60,
    'READY_AFTER': 2 * 60,
    'DELIVERED_AFTER': 3 * 60,
}