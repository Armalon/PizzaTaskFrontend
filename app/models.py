from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    address = db.Column(db.String(256), index=True, unique=True)
    phone = db.Column(db.String(20), index=True, unique=True)
    last_password_hash = db.Column(db.String(32))
    # denormalization bonuses
    # register_date
    # last_password_expires = db.Column(db.String(32))
    # denormalization orders_processed


    def __repr__(self):
        return '<User {}>'.format(self.username)