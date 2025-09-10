#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import requests
import bs4

from .flashcard import *
from .log import *

def get_set_url_from_id(id: str) -> str:
    # for whatever reason Quizlet wants a string after the id hence appending '/a/' to the url
    return f"https://quizlet.com/{id}/a/"

# Scrape the specified quizlet URL for a set of flashcards.
def scrape_quizlet_set(url: str) -> Set:
    # we only work with web pages that have the desired HTML elements
    if "quizlet.com" not in url:
        outwarn(f"Given url \"{url}\" probably not supported")

    headers = {
        # quizlet does not seem to accept HTTP requests without a user agent header...
        # this one seems to work well.
        "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
    }

    # send GET request + print response
    resp: requests.Response = requests.get(url, headers=headers)
    outnote(f"\"{url}\" responded with {resp.status_code}")

    soup = bs4.BeautifulSoup(resp.content, "html.parser")

    terms: list[str] = []
    definitions: list[str] = []

    # get all terms in the quizlet set
    for term in soup.select("a.SetPageTerm-wordText"):
        terms.append(term.get_text(strip = True, separator = "\n"))

    # same applies for definitions ofc
    for definition in soup.select("a.SetPageTerm-definitionText"):
        definitions.append(definition.get_text(strip = True, separator = "\n"))

    flashcards: list[Flashcard] = []

    # the amount of terms and definitions will (should?) always be equal.
    for i in range(len(terms)):
        # populate flashcards array
        flashcards.append(Flashcard(terms[i], definitions[i]))

    outlog(f"Recieved {len(flashcards)} flashcards from \"{url}\"")

    return Set(flashcards)
