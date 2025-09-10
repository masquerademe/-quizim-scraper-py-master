#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

# a class to represent a flashcard
class Flashcard:
    term: str
    definition: str

    def __init__(self, term: str, definition: str) -> None:
        self.term: str = term
        self.definition: str = definition

    # JSON-serialise the flashcard to be stored in a Flask session.
    def serialise(self) -> dict[str, str]:
        return {
            "term": self.term,
            "definition": self.definition
        }

# a class to represent a 'set' of flashcards
class Set:
    flashcards: list[Flashcard]

    def __init__(self, flashcards: list[Flashcard] = None) -> None:
        self.flashcards: list[Flashcard] = flashcards

    def serialise(self):
        ser_flashcards = list(map(lambda x: x.serialise(), self.flashcards))

        return {
            "flashcards": ser_flashcards
        }
