from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from comunidadeimpressionadora import routes