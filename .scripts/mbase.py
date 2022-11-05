import pathlib
import sys

DEBUG = True

def printd(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

PREF = str(pathlib.Path(__file__).absolute().parent.parent)+"/"
