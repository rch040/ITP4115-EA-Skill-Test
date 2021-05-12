from flask import Flask
from flask_login import LoginManager
from flask_appbuilder import SQLA, AppBuilder

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
appbuilder = AppBuilder(app, db.session)
from app import routes, models