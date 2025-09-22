# Modules

Although Jupyter notebooks are a great help for data exploration and explorative
programming, they aren't exactly the best option for code reuse.  You really
shouldn't end up copy/pasting cells between notebooks that contains your function
and class defintions.  These should be put in modules that can be imported into
your notebooks.

The `autoreload` extensiion helps you during development of such modules.  It
automatically reloads modules before executing user code, so that you don't have to
restart the kernel to see changes made to your modules.


## What is it?

1. `messages.py`: a Python module you are "developing".
1. `autoreload.ipynb`: a Jupyter notebook that uses the `messages` module and
   describes a scenario where autoreload is useful.
1. `autoreload.py`: paired Python script.
