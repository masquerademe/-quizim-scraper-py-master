#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import os
import flask
from .utils import *
from lib import *


#
## configure application

app = flask.Flask("quizimapp")

app.template_folder = dirs.templates(app.root_path)
app.static_folder = dirs.static(app.root_path)

# secret key for csrf protection
CSRF_SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = CSRF_SECRET_KEY

# session cookie config
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE="Lax"
)


#
## configure HTTP routes

# linked to compiled + bundled css file
STYLE_CSS_SRC = os.path.join(dirs.rel_compiled(), "style.css")

# favicon route for compatibility
@app.route("/favicon.ico")
def favicon() -> flask.Response:
    return flask.send_from_directory(dirs.image(app.root_path), "favicon.png")

# index: redirect to the homepage, assume javascript enabled
@app.route("/")
def index() -> flask.Response:
    return flask.render_template("index.html")

# home page
@app.route("/home")
def home() -> flask.Response:
    return flask.render_template("home.html", style_css_src=STYLE_CSS_SRC)

# flashcards learning page
@app.route("/flashcards", methods=["GET", "POST"])
def flashcards() -> flask.Response:
    if flask.request.method == "POST":
        # clear to avoid exceeding maximum session cookie size
        flask.session.clear()

        url = flask.request.data.decode("utf-8")
        set_session_cardset(scrape_quizlet_set(url))

        # id = flask.request.data.decode("utf-8")
        # set_session_setid(id)

        return flask.redirect(flask.url_for("flashcards"))

    return flask.render_template("flashcards.html", cardset=get_session_cardset(), setid=get_session_setid(), style_css_src=STYLE_CSS_SRC)
