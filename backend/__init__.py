from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os import path


DB_NAME = "database.db"     # Database file name
db = SQLAlchemy()           # SQLAlchemy database object
ma = Marshmallow()          # Marshmallow schema object


def create_app():
    """ Creates Flask app and sets its configurations """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "falsneicm382xlkd"
    app.config["SQLALCHEMY_DATABASE_URI"] =  f'sqlite:///{DB_NAME}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True
    db.init_app(app)
    ma.init_app(app)

    from .routes import routes
    app.register_blueprint(routes, url_prefix='/') #especify routes.py as routes file

    create_database(app) #create database file if it doesn't exist

    return app


def create_database(app):
    """ Creates new database file if it doesn't exist """
    if not path.exists('backend/' + DB_NAME):
        db.create_all(app=app)
        print('Database Created')  
