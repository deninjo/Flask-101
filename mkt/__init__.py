# defines the mkt directory as a package
# Initializes the package, sets up Flask app and database

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# creates the app object
app = Flask(__name__)

# Get the MySQL password from an environment variable
mysql_password = os.environ.get('MYSQL_PASSWORD')

# mysql db configuration
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'mysql+mysqlconnector://root:{mysql_password}@localhost:3306/market'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '5a740aa9280918d6a427e43c'

db = SQLAlchemy(app)

# to generate hashed passwords
bcrypt = Bcrypt(app)

# handles logins
login_manager = LoginManager(app)

# makes sure user logged in 2 view market page
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

#  register routes after app is created
from mkt import routes