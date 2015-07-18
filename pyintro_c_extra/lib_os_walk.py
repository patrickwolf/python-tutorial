'''
@summary: Python Intro - os.walk
'''
import os, sys

# If we are not given a path to list, use /tmp
if len(sys.argv) == 1:
    root = '/tmp'
else:
    root = os.path.normpath(sys.argv[1])
#Exercise set env variable in IDE

for dir_name, sub_dirs, files in os.walk(root):
    files.sort()
    for f in files:
        print os.path.join(dir_name, f)

# Exercise #1 print out sub folders instead of files
# Exercise #2 use tab \t to print out a directory tree