# UniversitySetup
Vim, latex setup for fast editing


Overview:

The application runs a Simple X Hotkey Daemon to handle keyboard shortcuts. The shortcuts are used to quickly manage folders and files. The main advantage is that of employing vimtex and ultisnips through vimplug thus speeding up typing of mathematical formulas. When a new lecture is created, it is opened in vim and vimtex automatically starts compiling master file every time you save the lecture. List of general snippets can be found in $BASE/.Ultisnips/tex.snippets. One can also create course-specific snippets in $BASE/{year}/{course}/.UltiSnips/tex.snippets. Latex has a preamble to speed up the process even further. It is shared within a yea and located in $BASE/{year}/.premble.tex.


Installation:

1) Download the files
2) Go inside the folder
3) run: sudo ./install.sh
4) follow the instructions


Usage:

- List of shortcuts:
  1) super + shift + c: select current course (can create a new one)
  2) super + shift + y: select current year (can create a new one)
  3) super + shift + v: select which lectures to include in the master file (One last lecture, two last lectures, all lectures or range {number}-{number}
  4) super + shift + l: select current lecture (can create a new one)
  5) super + shift + m: open master file pdf
  6) super + shift + r: open current course in file explorer
  7) super + shift + j: open current course in terminal
  8) super + shift + t: open theme selector for prompt menu
  9) super + shift + i: toggle current selection information


Useful links:
My inspiration: https://castel.dev/post/lecture-notes-1/
UltiSnips: https://github.com/SirVer/ultisnips
VimTex: https://github.com/lervag/vimtex
My email for suggestions: mailg9737@gmail.com
