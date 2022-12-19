from mbase import *
from aux import *
import re
import rofi
import sys
import subprocess
import datetime
from update_master import *

import notifypy

pref = PREF+"current-course/"
lectures = list(reversed(list(sorted(list_lectures(pref)))))
printd(lectures)

date_long = "%a %d %b %I:%M %p"
date_short = "%a %d %b"
def get_title(lec):
    f = open(pref+lec, "r")
    lines = f.readlines()
    f.close()
    for l in lines:
        #printd(l)
        res = re.match(r"\\lecture\{(.*?)\}\{(.*?)\}\{(.*)\}", l)
        if not res is None:
            print(res.group(2))
            #print(datetime.strptime(res.group(2), ))
            return "{number}. <b>{title}</b> <span size='smaller'>{date}</span>".format(number=res.group(1), title=res.group(3), date=datetime.datetime.strptime(res.group(2), date_long).strftime(date_short))

lecture_titles = [get_title(lec) for lec in lectures]
printd(lecture_titles)

tmp = {}
for t in lecture_titles:
    if t in tmp.keys():
        tmp[t] += 1
    else:
        tmp[t] = 1
for i, lec in enumerate(lectures):
    if tmp[lecture_titles[i]] > 1:
        lecture_titles[i] += " (" + lec + ")"
printd(lecture_titles)

option = rofi.select(prompt="Lecture", options=lecture_titles, rofi_options=["-markup-rows"])
printd(option)

if len(option) == 0:
    sys.exit(0)

lecture = 0
while lecture < len(lecture_titles):
    if lecture_titles[lecture] == option:
        break
    lecture += 1

if lecture == len(lecture_titles):
    lecture_id = "1" if len(lectures) == 0 else str(int(max(lectures)[4:-4])+1)
    printd(lecture_id)
    
    def to_len(s, n):
        return "0"*(n-len(s))+s if len(s) >= n else s[-n:]
    
    if len(str(int(lecture_id)-1)) < len(lecture_id):
        for l in lectures:
            if len(l[4:-4]) != len(lecture_id):
                subprocess.run(["mv", pref+l, pref+l[:4]+to_len(l[4:-4], len(lecture_id))+l[-4:]])
    
    lecture = "lec_"+lecture_id+".tex"
    f = open(pref+lecture,"w")
    tmp = "%! TEX root = " + os.path.realpath(pref) + "/master.tex\n\n\\lecture{" + lecture_id + "}{" + datetime.datetime.now().strftime(date_long) + "}{" + option + "}"
    printd(tmp)
    f.write(tmp)
    f.close()
    update_lectures()
else:
    lecture = lectures[lecture]

subprocess.run(["x-terminal-emulator", "-e", "vim", pref+lecture])
