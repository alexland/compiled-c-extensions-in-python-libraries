from distutils.core import setup, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy as NP

# create an Extension object with the appropriate name & sources
ext_module = Extension("tpl", 
		sources=["tpl.pyx", "lib/tpl.c"],
)


setup(
	name="wmod",
	ext_modules=cythonize([ext_module])
)
