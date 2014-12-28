from __future__ import print_function, division
from flask import Flask, render_template
import locale

locale.setlocale(locale.LC_ALL, 'en_GB.utf8')

app = Flask(__name__)


@app.route('/index.html')
def home():
    return render_template('home.html')


@app.route('/cv/')
def cv():
    return render_template('cv.html')


@app.route('/research/')
def research():
    return render_template('research.html')


@app.route('/projects/')
def projects():
    return render_template('projects.html')


# if __name__ == '__main__':
#     app.run(debug=True)
