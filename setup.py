#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import os
from setuptools import setup, find_packages

# util function used to read data from the README.md file for the long description.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="quizim",
    version="0.1.0",

    author="Jack Bennett",
    description="Import and learn Quizlet flashcards without Quizlet.",
    long_description=read("README.md"),
    license="MIT",
    url="https://github.com/kosude/quizim",

    packages=find_packages(),
)
