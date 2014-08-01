
generic directory structure of a cython package:

_note:_ wrapper.c is generated via cython

<pre>
.
+-- setup.py
+-- proj_dir
|	+-- \__init\__.py
|	+-- wrapper.pyx
|	+-- wrapper.c
|	+-- lib
|		+-- cfunc.c
|		+-- cfunc.h
+-- README.md
</pre>


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

to wrap a c function in a python package:

1. write the c function in a src file w/ a _c_ ext

2. write function prototype in a corresponding header file w/ _h_ ext

3. put both files in eg, a _lib_ directory

4. write the wrapper function in a _pyx_ file

4. put _pyx_ file same location as _lib_ dir

5. reference in _setup.py_

	i. 
	
	ii. 





building a cython extension from a .pyx file
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

method 2 (if no c-libraries required & no unusual build req)

* create .pyx file

* import pyximport; pyximport.install()

* import hw