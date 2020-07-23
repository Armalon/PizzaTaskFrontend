from app import db
from datetime import datetime

from sqlalchemy import func
import enum


class User(db.Model):
    # todo: add nullable=False fo fields
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

    @staticmethod
    def load_random_user():
        return User.query.order_by(func.random()).first()

    @staticmethod
    def load_user(user_id):
        return User.query.get(int(user_id))

    @staticmethod
    def load_user_by_phone(phone):
        return User.query.filter_by(phone=phone).first()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
        }

    def __repr__(self):
        return '<User {}>'.format(self.username)


class OrderStatus(enum.Enum):
    ORDERED = 'ORDERED'
    CONFIRMED = 'CONFIRMED'
    READY = 'READY'
    DELIVERED = 'DELIVERED'


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    products = db.relationship('ProductOrder', backref='order', lazy='dynamic')

    username = db.Column(db.String(64))
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))

    status = db.Column(db.Enum(OrderStatus))
    total_price = db.Column(db.Integer)

    # state enum(ordered, confirmed, cooked, delivered)
    # denormalization total_price
    # denormalization bonuses_earned

    @staticmethod
    def get_my_orders(user_id):
        return Order.query.filter_by(user_id=user_id).all()

    def __repr__(self):
        return f'<Order #{self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'product_orders': [product_order.to_dict() for product_order in self.products.all()],

            'user_name': self.username,
            'address': self.address,
            'phone': self.phone,

            'status': self.status.value if self.status is not None else '',
            'total_price': self.total_price,
        }


class ProductOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.relationship('Product')
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

    def to_dict(self):
        return {
            'quantity': self.quantity,
            'product': self.product.to_dict()
        }


class ProductType(enum.Enum):
    PIZZA = 'PIZZA'
    DRINK = 'DRINK'


class ProductSize(enum.Enum):
    LARGE = 'LARGE'
    MEDIUM = 'MEDIUM'
    SMALL = 'SMALL'


class PizzaBase(enum.Enum):
    WHITE = 'WHITE'
    RED = 'RED'


class PizzaCrust(enum.Enum):
    THIN = 'THIN'
    THICK = 'THICK'


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(ProductType))
    name = db.Column(db.String(64))
    description = db.Column(db.String(256))
    size = db.Column(db.Enum(ProductSize))
    weight = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    price = db.Column(db.Integer)
    picture = db.Column(db.String(64))
    base = db.Column(db.Enum(PizzaBase))
    crust = db.Column(db.Enum(PizzaCrust))
    # calories
    # search_result_order
    # is_recommended
    # is_available

    @staticmethod
    def get_by_filters(filters=None):
        # type, base, crust
        if filters is None:
            filters = {}

        return Product.query.filter_by(**filters).all()

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type.value,
            'name': self.name,
            'description': self.description,
            'size': self.size.value,
            'weight': self.weight,
            'volume': self.volume,
            'price': self.price,
            'picture': self.picture,
            'base': self.base.value,
            'crust': self.crust.value,
        }



