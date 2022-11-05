import sys
import yaml

def read(file):
    f = open(file,"r")
    data = yaml.safe_load(f)
    f.close()
    return data

def read_line(file, attr):
    return read(file).get(attr, "")
