#!/usr/bin/env python3
"""
This is a basic Flask application that displays a simple HTML page.

It defines a single route at the root URL ("/") and renders the index.html
template.

Usage:
    Run this script to start the Flask application:
    $ python3 0-app.py

Author:
    Your Name
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Configuration class for the Flask app.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    Retrieve the user information based on the user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        dict or None: The user dictionary if found, None otherwise.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Function executed before handling each request.

    It retrieves the logged-in user based on the `login_as` URL parameter and
    sets it as a global variable on `flask.g`.
    """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@app.route('/')
def index():
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('5-index.html', gettext=gettext)


if __name__ == '__main__':
    app.run()
