from flask_frozen import Freezer
from elliotmarsden import app

freezer = Freezer(app)

if __name__ == '__main__':
    app.debug = False
    app.testing = True
    freezer.freeze()
