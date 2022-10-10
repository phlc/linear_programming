from re import M
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os import path

DB_NAME = "database.db"
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "falsneicm382xlkd"
    app.config["SQLALCHEMY_DATABASE_URI"] =  f'sqlite:///{DB_NAME}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True
    db.init_app(app)
    ma.init_app(app)

    from .routes import routes
    app.register_blueprint(routes, url_prefix='/')

    create_database(app)

    return app


def create_database(app):
    if not path.exists('backend/' + DB_NAME):
        db.create_all(app=app)
        print('Database Created')  
