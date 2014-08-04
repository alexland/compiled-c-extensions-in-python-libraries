from setuptools import setup, Extension
from Cython.Distutils import build_ext
import numpy as NP

'''
NP.get_include() returns the location of the headerfiles such as
arrayobject.h; on my mbp it is:
/usr/local/Cellar/python3/3.4.1/Frameworks/Python.framework/
Versions/3.4/lib/python3.4/site-packages/numpy/core/include/numpy
'''


NAME = "arraycomp"
VERSION = "0.1"
DESCR = "template for building python extensions that wrap C code via cython"
URL = "https://github.com/alexland/"
REQUIRES = ['numpy', 'cython']
AUTHOR = "doug ybarbo"
EMAIL = "dougybarbo@yahoo.com"

LICENSE = "MIT"

SRC_DIR = "cwrap"
PACKAGES = [SRC_DIR]

ext_1 = Extension(SRC_DIR + ".cfns",
                  [SRC_DIR + "/lib/cfunc.c", SRC_DIR + "/cfns.pyx"],
                  libraries=[],		# libs in stnd lib search path to link against
				  library_dirs=[],	# if libraries above in non-stnd location
				  runtime_library_dirs=[], # search for sharted libraries at runtime
                  include_dirs=[NP.get_include()])

EXTENSIONS = [ext_1]

if __name__ == "__main__":
    setup(install_requires=REQUIRES,
          packages=PACKAGES,
          zip_safe=False,
          name=NAME,							# name of the installation tarball
          version=VERSION,						# appended to end of tarball name
          description=DESCR,
          author=AUTHOR,
          author_email=EMAIL,
          url=URL,
          license=LICENSE,
          cmdclass={"build_ext": build_ext},
          ext_modules=EXTENSIONS
          )
