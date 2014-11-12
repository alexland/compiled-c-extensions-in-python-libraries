from distutils.core import setup
from setuptools import setup, Extension
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as NP

NAME = "cython-tpl5"
VERSION = "0.1"
DESCR = "template for wrapping c code w cython"
URL = "http://www.github.com"
REQUIRES = ["numpy", "cython"]

AUTHOR = "doug ybarbo"
AUTHOR_EMAIL = "doug.ybarbo@gmail.com"

LICENSE = "MIT"

SRC_DIR = "cython-proj"
PACKAGES = [SRC_DIR]

ext_1 = Extension(SRC_DIR + ".wrapped",
					[SRC_DIR + "/lib/sample.c", SRC_DIR + "/wrapped.pyx"],
					libraries=[],
					include_dirs=[NP.get_include()])

EXTENSIONS = [ext_1]


if __name__ == "__main__":
	setup(install_requirements=REQUIRES,
			packages=PACKAGES,
			zip_safe=False,
			name=NAME,
			version=VERSION,
			description=DESCR,
			author=AUTHOR,
			author_email=EMAIL,
			url=URL,
			license=LICENSE,
			cmdclass={"build_ext": build_ext},
			ext_modules=EXTENSIONS)

ext_modules = [
    Extension("sample", 
              ["wrapped.pyx"],
              include_dirs=['..'],
              libraries=[],
              library_dirs=['..'])]
setup(
  name = 'Sample extension module',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
