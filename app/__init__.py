"""
    App initialiazer, sets up DB, LoginMangers, Logging etc.
    Imports views models that are used
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask_login import LoginManager
import logging
from logging.handlers import RotatingFileHandler
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)

# Setup logging
# Eventually use the logging_config.ini
# Not a huge deal though
handler = RotatingFileHandler('/var/log/recording.log')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# Set up DB using sqlAlchemy
engine = create_engine( "mysql://dsumar200@/uploadTest")
if not database_exists(engine.url):
    create_database(engine.url)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://dsumar200@/uploadTest"
app.db = SQLAlchemy(app)


# Add WTF secret key
app.secret_key = "secret_key"

# # Login handler
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

from app import views
from .forms import SampleForm
# from auth import models, views

# Create DB tables if not created
app.db.create_all()
app.db.session.commit()
