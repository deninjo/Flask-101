# imports everything step by step to prevent circular imports 2 execute our app

from mkt import app

if __name__ == '__main__':
    app.run(debug=True)