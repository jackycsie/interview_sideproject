# controllers.py
from .models import db, User, Product
from werkzeug.exceptions import NotFound

def create_user(id, points, cash):
    user = User(id=id, points=points, cash=cash)
    db.session.add(user)
    db.session.commit()
    return user

def get_user(id):
    user = User.query.get(id)
    if user is None:
        raise NotFound("User {} doesn't exist".format(id))
    return user

def delete_user(id):
    user = User.query.get(id)
    if user is None:
        raise NotFound("User {} doesn't exist".format(id))
    db.session.delete(user)
    db.session.commit()

def purchase_product(user_id, product_id):
    user = User.query.get(user_id)
    if user is None:
        raise NotFound("User {} doesn't exist".format(user_id))
    product = Product.query.get(product_id)
    if product is None:
        raise NotFound("Product {} doesn't exist".format(product_id))

    if product.can_be_exchanged and user.points >= product.points:
        user.points -= product.points
    elif not product.can_be_exchanged and user.cash >= product.price:
        user.cash -= product.price
        user.points += product.points
    else:
        raise ValueError("Not enough resources to purchase product")

    db.session.commit()

