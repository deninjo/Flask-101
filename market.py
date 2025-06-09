from flask import Flask, render_template

app = Flask(__name__)


# two routes for single html file
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


# market page route + sending data to templates
@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', item_name=items) # referenced w {{item_name}} in html



# Check if this file is being run directly (not imported as a module)
if __name__ == "__main__":
    # Start the Flask development server
    app.run(debug=True)
