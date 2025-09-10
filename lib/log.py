#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import colorama
import sys

colorama.init()

# send log output to stdout
def outlog(s: str, **kwargs):
    print(f"[Quizim] {s}", **kwargs, file = sys.stdout)

# send notification output to stdout
def outnote(s: str, **kwargs):
    print(f"{colorama.Fore.BLUE}[Quizim] {s}{colorama.Style.RESET_ALL}", **kwargs, file = sys.stdout)

# send warning output to stdout
def outwarn(s: str, **kwargs):
    print(f"{colorama.Fore.YELLOW}[Quizim] WARN: {s}{colorama.Style.RESET_ALL}", **kwargs, file = sys.stdout)

# send error message to stderr
def outerror(s: str, **kwargs):
    print(f"{colorama.Fore.RED}[Quizim] ERROR: {s}{colorama.Style.RESET_ALL}", **kwargs, file = sys.stderr)

# send fatal error message to stderr
def outfatal(s: str, **kwargs):
    print(f"{colorama.Fore.RED}{colorama.Back.YELLOW}[Quizim] FATAL: {s}{colorama.Style.RESET_ALL}", **kwargs, file = sys.stderr)
    exit(0)
