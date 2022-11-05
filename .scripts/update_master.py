from mbase import *
from aux import *
import re

lecture_options = ["Last lecture", "Last two lectures", "All lectures", b"(\d+)-(\d)+"]
lecture_actions = [lambda x, res: x[-1:], lambda x, res: x[-2:], lambda x, res: x[:], lambda x, res: list(filter(lambda x: int(res.group(1)) <= int(x[4:-4]) and int(x[4:-4]) <= int(res.group(2)), x))]

def update_lectures():
    pref=PREF+"current-course/"
    f = open(pref+"master.tex", "r")
    data = f.readlines()
    printd(data[13])
    f.close()
    lectures = list(sorted(list_lectures(pref)))
    option = data[13][6:-1]
    printd(option)
    for i, opt in enumerate(lecture_options):
            if type(opt) == type(b"a"):
                opt = opt.decode()
            res = re.match(opt, option)
            if not res is None and res.span() == (0,len(option)):
                printd(lectures)
                lectures = lecture_actions[i](lectures, res)
                printd(lectures)
    data = data[:14] + ["    \\input{"+pref+l+"}\n" for l in lectures] + data[-2:]
    printd(data)
    f = open(pref+"master.tex", "w")
    f.writelines(data)
    f.close()

