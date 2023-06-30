from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views import api_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configure database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:testlab@db:3306/test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600  # 例如，設置為 1 小時

    db.init_app(app)

    @app.teardown_appcontext
    def teardown_db(exception=None):
        db.session.remove()

    app.register_blueprint(api_bp, url_prefix='/api')

    return app
