from distutils import extension
from flask import Flask
from .config import DevConfig
from app import views
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

def create_app(config_name):
    app = Flask(__name__)
    # Setting up configuration
    app.config.from_object(DevConfig)

    bootstrap = Bootstrap()
    db = SQLAlchemy()

    # initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
