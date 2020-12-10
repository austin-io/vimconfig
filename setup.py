#!/bin/python3

import os
import shutil

home = os.path.expanduser("~")
colorsPath = os.path.join(home,".vim/colors")
vimrcPath = os.path.join(home,".vimrc")

# Create folders for colors
os.makedirs(colorsPath, exist_ok=True)

# Move codedark.vim into colors directory
shutil.copyfile(os.getcwd() + "/codedark.vim", colorsPath + "/codedark.vim")

# Replace .vimrc file
shutil.copyfile(os.getcwd() + "/.vimrc", home + "/.vimrc")
