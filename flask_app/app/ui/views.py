from flask import render_template, send_from_directory
from . import ui


@ui.route("/")
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template("ui/home.html", title="Welcome")


@ui.route('/assets/<path:filename>')
def assets_static(filename):
    """
    Inner links walkaround for angular assets
    """
    return send_from_directory('static/ang/assets/', filename)