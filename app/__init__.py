from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app import routes, models

#set to the name of the module being used
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # represents the database
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
