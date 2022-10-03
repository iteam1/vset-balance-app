from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a745e111cf3b161c90630fc2ae745351'

# import all routes
from root import routes