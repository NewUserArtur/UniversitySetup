import yaml_func
from mbase import *
from aux import *
import rofi
import subprocess
import os
import sys
import pathlib

pref = PREF+"current-year/"

courses = listdir_visible(pref)
printd(courses)

course_titles = [yaml_func.read_line(pref+course+"/info.yaml", "title") for course in courses]
printd(course_titles)

tmp = {} 
for i in range(len(course_titles)):
    if not course_titles[i] in tmp.keys():
        tmp[course_titles[i]] = 1
    else:
        tmp[course_titles[i]] += 1
for i in range(len(course_titles)):
    if tmp[course_titles[i]] > 1 or len(course_titles[i]) == 0:
        course_titles[i] += " (" + courses[i] + ")"

option = rofi.select("Course", course_titles)
printd(option)

if len(option) == 0:
    sys.exit(0)
 
course = 0
while course < len(course_titles) and course_titles[course] != option:
    course += 1
printd(course)

if course == len(course_titles):
    ok = 0
    while ok < 2:
        fld_name = rofi.prompt("Enter folder name", [] if ok == 0 else ["-mesg", "The name you entered might be inv    alid"])
        printd(fld_name)
        if len(fld_name) == 0:
            sys.exit(0)
        ok = 2
        try:
            os.mkdir(pref+fld_name)
        except Exception as exc:
            printd(exc)
            ok = 1
    
    os.mkdir(pref+fld_name+"/.UltiSnips")
    os.mkdir(pref+fld_name+"/figures")
    pathlib.Path(pref+fld_name+"/.UltiSnips/tex.snippets").touch()

    f = open(pref+fld_name+"/info.yaml", "w")
    f.write("title: '" + option + "'")
    f.close()
    
    f = open(PREF+".templates/master.tex", "r")
    data = f.read()
    f.close()
    data = data.replace("{%#1}", PREF+"current-year").replace("{%#2}", option)
    f = open(pref+fld_name+"/master.tex", "w")
    f.write(data)
    f.close()

    course = fld_name
else:
    course = courses[course]

subprocess.run(["ln", "-nsf", pref+course, PREF+"current-course"])
