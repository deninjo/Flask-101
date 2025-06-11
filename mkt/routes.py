from mkt import app
from flask import render_template
from mkt.models import Item

# two routes for single html file
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


# market page route + sending data to templates
@app.route('/market')
def market_page():
    items = Item.query.all()  # Get all items from DB
    return render_template('market.html', item_name=items) # referenced w {{item_name}} in html
