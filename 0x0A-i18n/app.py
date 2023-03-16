#!/usr/bin/env python3
"""
Flask app
"""
from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Config for languages """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """ Return index """
    return render_template('index.html')


@babel.localeselector
def get_locale():
    """ Get locale selector for babel """
    locale = request.args.get('locale')
    if locale:
        lang = locale
    elif g.user and g.user['locale'] in app.config['LANGUAGES']:
        lang = g.user['locale']
    else:
        lang = request.accept_languages.best_match(app.config['LANGUAGES'])
    return lang


def get_user():
    """ Get user or return None """
    loggin_as = request.args.get('login_as')
    if not loggin_as:
        return None
    user = int(loggin_as)
    return users.get(user) if user in users else None


def fmt_timezone():
    """ Return current time with format """
    timezone = get_timezone()
    loc_dt = timezone.localize(datetime.utcnow())
    return loc_dt.strftime('%b %d, %Y %H:%M:%S')


@app.before_request
def before_request():
    """ before request for user """
    g.user = get_user()
    g.current_time = fmt_timezone()


def checked_timezone(time_zone: str):
    """ Validated timezone """
    try:
        return timezone(time_zone)
    except UnknownTimeZoneError:
        return None


@babel.timezoneselector
def get_timezone():
    """
    Get timezone it's depents of follow requirements
    1.- Find timezone parameter in URL parameters
    2.- Find time zone from user settings
    3.- Default to UTC
    """
    timezone = request.args.get('timezone')
    if timezone:
        check = checked_timezone(timezone)
    elif g.user and g.user['timezone']:
        check = checked_timezone(g.user['timezone'])
    else:
        check = app.config['BABEL_DEFAULT_TIMEZONE']
    return check if check else app.config['BABEL_DEFAULT_TIMEZONE']
