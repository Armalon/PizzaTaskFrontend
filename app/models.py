from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=False)
    address = db.Column(db.String(256), index=True, unique=False)
    register_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    phone = db.Column(db.String(20), index=True, unique=True)
    last_password_hash = db.Column(db.String(32))
    # todo: Change to tomething like UTCNOW + 86400 seconds
    last_password_expires_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    orders = db.relationship('Order', backref='customer', lazy='dynamic')

    # denormalization bonuses
    # denormalization orders_processed


    def __repr__(self):
        return '<User {}>'.format(self.username)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # state enum(ordered, confirmed, cooked, delivered)
    # denormalization total_price
    # denormalization bonuses_earned

    def __repr__(self):
        return f'<Order #{self.id}>'
