from mbase import *
import rofi
import sys
import re
from aux import *
from update_master import *

ok = 0
msg = ""
pref = PREF+"current-course/"
lectures = list(sorted(list_lectures(pref)))
while ok == 0:
    option = rofi.select("Lectures", list(filter(lambda o: type(o)==type("s"), lecture_options)), [] if len(msg) == 0 else ["-mesg", msg])
    ok = 1
    printd(option)
    if len(option) == 0:
        sys.exit(0)

    for opt in lecture_options:
        if type(opt) == type(b"a"):
            opt = opt.decode()
        res = re.match(opt, option)
        if not res is None and res.span() == (0,len(option)):
            ok = 1
    msg = "Invalid input"

f = open(pref+"master.tex", "r")
data = f.readlines()
f.close()
data = data[:13] + [data[13][:6]+option+"\n"] + data[14:]
printd(data)
f = open(pref+"master.tex", "w")
f.writelines(data)
f.close()
update_lectures()
