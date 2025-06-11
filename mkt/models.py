from mkt import db

# Creating the Item Model - python class that represents a database table.
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=20), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description =  db.Column(db.String(length=1000), nullable=False)

    # shows the item’s name when printed (for debugging).
    def __repr__(self):
        return f'Item > {self.name}'