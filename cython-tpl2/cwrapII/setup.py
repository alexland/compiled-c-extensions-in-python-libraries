
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("array_clip", 
              ["array_clip.pyx"])
]

setup(
  name = 'array_clip app',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
