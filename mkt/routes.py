# contains decorator patterns - route funcs 

from mkt import app
from flask import render_template, redirect, url_for, flash
from mkt.models import Item, User
from mkt.forms import RegisterForm
from mkt import db

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


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    
    if form.errors != {}: # If there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    
    return render_template('register.html', form=form)