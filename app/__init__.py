from flask import Flask
from .config import DevConfig
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
# Setting up configuration
app.config.from_object(DevConfig)

from app import views
db = SQLAlchemy()