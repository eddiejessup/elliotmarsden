from __future__ import print_function, division
from flask import Flask, render_template
import locale

locale.setlocale(locale.LC_ALL, 'en_GB')

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.jinja')


@app.route('/cv')
def cv():
    return render_template('cv.jinja')


@app.route('/research')
def research():
    return render_template('research.jinja')


@app.route('/projects')
def projects():
    return render_template('projects.jinja')


if __name__ == '__main__':
    app.run(debug=True)
