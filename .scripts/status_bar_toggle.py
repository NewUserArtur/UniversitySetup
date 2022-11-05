from mbase import *
from aux import *
import subprocess

if len(subprocess.run(["pgrep", "-f", "tint2"], stdout=subprocess.PIPE).stdout) == 0:
    subprocess.Popen(["tint2", "-c", PREF+".config/tint2rc"], shell=False)
else:
    subprocess.Popen(["pkill", "-f", "tint2"], shell=False)
