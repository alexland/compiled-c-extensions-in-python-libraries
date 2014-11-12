
from distutils.core import setup
from Cython.Build import cythonize


setup(name="compiled ext module I",
		ext_modules=cythonize("hw.pyx"),
)