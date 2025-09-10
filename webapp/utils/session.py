#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import flask

from lib import Set

# get the flashcard set stored in the current session
def get_session_cardset() -> dict[str, str]:
    return flask.session.get("flashcard-set")

# get current imported set ID from session
def get_session_setid() -> str:
    return flask.session.get("flashcard-set-id") or ""

# store the given cardset in the current session
def set_session_cardset(cardset: Set):
    flask.session["flashcard-set"] = cardset.serialise()

# set current imported set ID in session
def set_session_setid(setid: str):
    flask.session["flashcard-set-id"] = setid
