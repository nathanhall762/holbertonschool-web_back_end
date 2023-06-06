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
from flask import Flask, render_template, request
from flask_babel import Babel

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


@app.route('/')
def index():
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """
    Determine the best match for the supported languages based on client's
    preferences.

    Returns:
        str: Best match language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
