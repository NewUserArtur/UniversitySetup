from mbase import *
import os
import subprocess

def listdir_visible(path):
    return list(filter(lambda x: x[0]!='.', os.listdir(path)))

def list_lectures(path):
    return list(filter(lambda x: len(x)>8 and x[:4] == "lec_" and x[-4:] == ".tex", os.listdir(path)))
