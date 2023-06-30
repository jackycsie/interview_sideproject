# views.py
from flask import Blueprint, request
from flask_restx import Api, Resource
from flask_restx import fields
from .controllers import create_user, get_user, delete_user, purchase_product

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

user_model = api.model('User', {
    'id': fields.String(required=True, description='The user ID'),
    'points': fields.Integer(required=False, description='User points', default=0),
    'cash': fields.Float(required=False, description='User cash', default=0.0)
})

@api.route('/user')
class UserResource(Resource):
    @api.expect(user_model, validate=True)
    def post(self):
        data = request.get_json()
        id = data.get('id')
        points = data.get('points', 0)
        cash = data.get('cash', 0.0)
        user = create_user(id, points, cash)
        return {'id': user.id, 'points': user.points, 'cash': user.cash}, 201

@api.route('/user/<string:id>')
class UserIdResource(Resource):
    def get(self, id):
        user = get_user(id)
        return {'id': user.id, 'points': user.points, 'cash': user.cash}

    def delete(self, id):
        delete_user(id)
        return '', 204

@api.route('/user/<string:user_id>/purchase/<string:product_id>')
class PurchaseResource(Resource):
    def post(self, user_id, product_id):
        purchase_product(user_id, product_id)
        user = get_user(user_id)
        return {'id': user.id, 'points': user.points, 'cash': user.cash}, 201

