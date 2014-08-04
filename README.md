
generic directory structure of a cython package:



<pre>
top-level (distribution root)

+-- proj_dir
|	+-- __init__.py
|	+-- wrapper.pyx
|	+-- wrapper.c
|	+-- lib
|		+-- cfunc.c
|		+-- cfunc.h
+-- setup.py
+-- MANIFEST.in
+-- runner
+-- README.md
</pre>

_note_ wrapper.c is generated via cython

_note_ the importable module is created inside proj_dir, & is a .so file
	which is imported like a normal python module


steps:

```
    cd proj_dir    				# 1 level deep
```
```
    cython wrapper.pyx  		# cythonize the C src, creates 'wrapper.c'
```
```
    cd ..						# go up to root dir
```
```
    python3 setup.py develop	# build python package 
```





========

_to wrap c functions in a python package:_

1. write the c functions in a src file w/ a _c_ ext

2. write function prototypes in a corresponding header file w/ _h_ ext

3. put both files in eg, a _lib_ directory

4. write the wrapper function in a _pyx_ file

4. put _pyx_ file same location as _lib_ dir

5. reference in __init.py__



### building a cython extension from a .pyx file
======

method 1

* code .pyx file

* create setup.py file 

```python 
from distutils.core import setup
from Cython.Build import cythonize
		
setup(name="compiled ext module I",
		ext_modules=cythonize("hw.pyx"),
)
```

* from shell:
    $> python3 setup.py build-ext --inplace
	
* this will build a .so file, which can be imported and its fns called inside this namespace, like so:

* import hw

============

method 2 (if no C libraries required & no unusual build req)

* create .pyx file

* import pyximport; pyximport.install()

* import hw