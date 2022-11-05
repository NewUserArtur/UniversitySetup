from mbase import *
import yaml_func

print("Current course: {}".format(yaml_func.read_line(PREF+"current-course/info.yaml", "title")))
