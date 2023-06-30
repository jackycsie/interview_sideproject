from flask import Flask, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from .views import api_bp

import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__ , static_folder='frontend/static', static_url_path='/static')

    # Configure database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:testlab@db:3306/test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600  # 例如，設置為 1 小時

    db.init_app(app)

    @app.teardown_appcontext
    def teardown_db(exception=None):
        db.session.remove()

    app.register_blueprint(api_bp, url_prefix='/api')

    # Create a new blueprint for the frontend
    current_path = os.path.dirname(os.path.realpath(__file__))
    frontend_bp = Blueprint('frontend', __name__, static_folder=os.path.join(current_path, 'frontend/static'), template_folder=os.path.join(current_path, 'frontend/templates'))

    @frontend_bp.route('/')
    def index():
        return render_template('index.html')

    # Register the frontend blueprint
    app.register_blueprint(frontend_bp)

    return app
