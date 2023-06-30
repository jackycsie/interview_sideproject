from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String(64), primary_key=True)
    points = db.Column(db.Integer, nullable=False, default=0)
    cash = db.Column(db.Float, nullable=False, default=0.0)

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0.0)
    points = db.Column(db.Integer, nullable=False, default=0)
    can_be_exchanged = db.Column(db.Boolean, default=False)
