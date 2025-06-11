# defines the mkt directory as a package
# allowing imports from that directory

import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Get the MySQL password from an environment variable
mysql_password = os.environ.get('MYSQL_PASSWORD')

# mysql configuration
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'mysql+mysqlconnector://root:{mysql_password}@localhost:3306/market'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from mkt import routes