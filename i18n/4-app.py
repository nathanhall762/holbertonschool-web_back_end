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


@babel.localeselector
def get_locale():
    """
    Determine the best match for the supported languages based on client's preferences.

    Returns:
        str: Best match language code.
    """
    # Check if the locale parameter is present in the URL
    if 'locale' in request.args:
        requested_locale = request.args.get('locale')
        # Check if the requested locale is supported
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale

    # Fallback to the default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('4-index.html', gettext=gettext)


if __name__ == '__main__':
    app.run()
