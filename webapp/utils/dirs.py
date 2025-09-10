#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import os

# static/ folder path.
# Includes SCSS, JS, etc...
def static(root_path: str) -> str:
    return os.path.join(root_path, "static")

# static/img/ folder path.
# includes image resources
def image(root_path: str) -> str:
    return os.path.join(root_path, "static", "img")

# views/ folder path.
# includes HTML/jinja2 components and templates.
def templates(root_path: str) -> str:
    return os.path.join(root_path, "views")

# relative compiled output folder path.
# e.g. CSS (compiled from SCSS)
def rel_compiled() -> str:
    return os.path.join("static", "out")
