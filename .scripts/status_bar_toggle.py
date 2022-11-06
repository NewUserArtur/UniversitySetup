from mbase import *
from aux import *
import subprocess
import notifypy
import yaml_func

"""
if len(subprocess.run(["pgrep", "-f", "tint2"], stdout=subprocess.PIPE).stdout) == 0:
    subprocess.Popen(["tint2", "-c", PREF+".config/tint2rc"], shell=False)
else:
    subprocess.Popen(["pkill", "-f", "tint2"], shell=False)
"""

note = notifypy.Notify()
note.title = "Info"
note.application = "University scheduler"
note.message = "Current course: {}".format(yaml_func.read_line(PREF+"current-course/info.yaml", title))
note.send()
