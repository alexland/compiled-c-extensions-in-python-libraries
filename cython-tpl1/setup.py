from setuptools import setup, Extension
from Cython.Distutils import build_ext
import numpy as NP

NAME = "cwrapI"
VERSION = "0.1"
DESCR = "template for building python extensions that wrap C code via cython"
URL = "https://github.com/alexland/"
REQUIRES = ['numpy', 'cython']

AUTHOR = "doug ybarbo"
EMAIL = "dougybarbo@yahoo.com"

LICENSE = "MIT"

SRC_DIR = "cwrapI"
PACKAGES = [SRC_DIR]

ext_1 = Extension(SRC_DIR + ".wrapper",
                  [SRC_DIR + "/lib/cfunc.c", SRC_DIR + "/wrapper.pyx"],
                  libraries=[],
                  include_dirs=[NP.get_include()])


EXTENSIONS = [ext_1]

if __name__ == "__main__":
    setup(install_requires=REQUIRES,
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
          ext_modules=EXTENSIONS
          )
