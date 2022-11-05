import yaml_func
from mbase import *
import rofi
import subprocess
import os
import sys

print(PREF)
years = list(filter(lambda x: x[0]!='.' and x != "current-year" and x != "current-course", os.listdir(PREF)))
printd(years)

ok = 0
while ok < 2:
    fld_name = rofi.select(prompt="Year", options=years, rofi_options=[] if ok == 0 else ["-mesg", "Could not create a folder"])
    printd(fld_name)
    if len(fld_name) == 0:
        sys.exit(0)
    ok = 2
    year = 0
    while year < len(years) and years[year] != fld_name:
        year += 1
    if year == len(years):
        try:
            os.mkdir(PREF+fld_name)
            f = open(PREF+".templates/preamble.tex", "r")
            data = f.read()
            f.close()
            printd(PREF+fld_name+"/.preamble.tex")
            f = open(PREF+fld_name+"/.preamble.tex", "w")
            f.write(data)
            f.close()
        except Exception as exc:
            printd(exc)
            ok = 1

subprocess.run(["ln", "-nsf", PREF+fld_name, PREF+"current-year"])
