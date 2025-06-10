from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DB Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite-market.db'
db = SQLAlchemy(app)


# Creating the Item Model - python class that represents a database table.
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=20), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description =  db.Column(db.String(length=1000), nullable=False, unique=True)

    # shows he item’s name when printed (for debugging).
    def __repr__(self):
        return f'Item {self.name}'


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



# Check if this file is being run directly (not imported as a module)
if __name__ == "__main__":
    # Start the Flask development server
    app.run(debug=True)
