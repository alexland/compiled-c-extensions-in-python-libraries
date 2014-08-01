
generic directory structure of a cython package:

[_note:_ wrapper.c is generated via cython]

steps:

%> cd proj_dir

%> cython wrapper.pyx

%> cd ..

%> python3 setup.py develop

proj_name
		|__ setup.py
		|
		|__ README.md
		|
		|== proj_dir
				|__ __init__.py
				|
				|__ wrapper.c   _cython-generated_
				|
				|__ wrapper.pyx
				|
				|== lib
					|__ cfunc.c
					|
					|__ cfunc.h






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