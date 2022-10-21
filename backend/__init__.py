from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os import path
from flask_cors import CORS

DB_NAME = "database.db"     # Database file name
db = SQLAlchemy()           # SQLAlchemy database object
ma = Marshmallow()          # Marshmallow schema object

CORS_ALLOW_ORIGIN="*,*"
CORS_EXPOSE_HEADERS="*,*"
CORS_ALLOW_HEADERS="content-type,*"


def create_app():
    """ Creates Flask app and sets its configurations """
    app = Flask(__name__)
    cors = CORS(app, origins=CORS_ALLOW_ORIGIN.split(","), allow_headers=CORS_ALLOW_HEADERS.split(",") , expose_headers= CORS_EXPOSE_HEADERS.split(","),   supports_credentials = True)
    app.config['CORS_HEADERS'] = 'Content-Type'
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
    if not path.exists(path.join('backend', DB_NAME)):
        db.create_all(app=app)
        print('Database Created')  
