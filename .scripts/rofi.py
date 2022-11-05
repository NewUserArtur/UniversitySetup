import subprocess
import os

def rofi_base(opt, inp):
    basic_options = ["rofi", "-no-levenshtein-sort", "-dmenu", "-format", "s", "-i"]
    res = subprocess.run(basic_options+opt, input=inp, stdout=subprocess.PIPE, universal_newlines=True)
    return res.stdout.strip()

def select(prompt="", options=[], rofi_options=[]):
    return rofi_base(["-l", "5", "-p", prompt]+rofi_options, "\n".join(map(str, options)))

def prompt(prompt="", rofi_options=[]):
    return rofi_base(["-l", "0", "-p", prompt]+rofi_options, "")
