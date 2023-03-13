#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config for languages """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """ Return index """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """ Get locale selector for babel """
    return request.accept_languages.best_match(app.config['LANGUAGES'])
