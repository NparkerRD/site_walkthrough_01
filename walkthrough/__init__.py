from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///walkthrough01.db'
app.config['SECRET_KEY'] = '95f4c57836359d65a7471742'
db = SQLAlchemy(app)
app.app_context().push()

from walkthrough import routes
