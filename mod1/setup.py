from distutils.core import setup, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy as NP

"""
this extension module can be imported like so:

>>> import tpl as TPL

and the functions w/in this namespace called like so

>>> TPL.divide(567, 4)

"""


# create an Extension object with the appropriate name & sources
ext_module = Extension("tpl", 
		sources=["tpl.pyx", "lib/tpl.c"],
)


setup(
	name="wmod",
	ext_modules=cythonize([ext_module])
)
