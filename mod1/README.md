
this is pretty close the bar minimum you need to create a compiled extension in python from C code.

the components:

* setup.py

* __init__.py

* lib/

  * source.c
  * header.h
  
* extmod.pyx

* cextmod.pxd


===========

_*setup.py*_

these two import lines, both from cython, are crucial:

from Cython.Build import cythonize
from Cython.Distutils import build_ext


_*__init__.py*_

for building python modules, this file of course can be empty; for a compiled extension 
it can't be empty