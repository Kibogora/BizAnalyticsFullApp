from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
username = 'test'
password = 'test'

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@localhost/kibogora'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # Import models here to avoid circular imports
        from application.models.users import User, Datasets
        db.create_all()

    return app
