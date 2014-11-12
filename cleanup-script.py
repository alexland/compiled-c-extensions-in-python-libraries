#!/usr/local/bin/python3

import os
import sys
import shutil

"""
(i) descend one level (cd into the top-level dir)
(ii) change permissions for 'build' dir
(iii) delete the 'build' directory
(iv) identify only directory remaining
(v) change permissions for this dir
(vi) descend one level ('cwraps') to this directory
(v) delete:
	__pycache__
	*.c
	*.so

file permissions notes:

%> ls -eGnO

"""

local('sudo find dir -exec chown name {} \;')

chown -R user-id:group-id /path/to/directory

ddir = os.path.expanduser('~/Projects/compiled-c-extensions-in-python-libraries/cython-tpl1)

build_dir = os.path.join(ddir, 'build')

if os.path.exists(build_dir):
	
	shutil.chown(build_dir, user='$USER')
	shutil.rmtree()



os.listdir(path='.')

os.removedirs('build')

ddir = 


