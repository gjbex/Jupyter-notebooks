# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     notebook_metadata_filter: kernelspec,language_info
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.13.5
# ---

# %% [markdown]
# # Magic

# %%
import matplotlib.pyplot as plt
import numpy as np

# %% [markdown]
# Jupyter Notebook, Jupyter Lab and iPython have several non-Python "magic" commands that help you work more efficiently in these environments.

# %% [markdown]
# ## History

# %% [markdown]
# As cells can be executed in any order, the command history is not necessarily the same as a top to bottom view of the notebook.

# %%
x = np.linspace(0.0, 1.0, 101)

# %%
y = np.sqrt(x)

# %% [markdown]
# You can get the history of the current session using the `%hist` magic command.

# %%
# %hist -n

# %% [markdown]
# You can specify a range of lines to be shown.

# %%
# %hist 2-3

# %% [markdown]
# The output of the previous command is stored in `_`, and hence can be reused in subsequent commands.  Although this can be convenient, it should not be over-used since it makes the execution very brittle.

# %%
np.random.uniform(5)

# %%
_**2


# %%
def plot_function(n: int) -> None:
    x_values = np.linspace(0.0, 1.0, n)
    y_values = np.sqrt(x)
    _ = plt.plot(x, y)


# %% [markdown]
# ## Keeping track

# %% [markdown]
# To keep track of the modules loaded and the variables defined, you can use the `%whos` magic.  This can be useful while debugging to catch a typo in a variable name.

# %%
# %whos

# %% [markdown]
# The `%psearch` magic lets you find specific objects.

# %%
# %psearch plot*

# %%
# %psearch p* module

# %%
# %psearch plt.x* function

# %% [markdown]
# If the source code of a Python function is available, you can display it easily using `%psource`.

# %%
import gcd

# %%
# %psource gcd.gcd

# %% [markdown]
# ## Cleaning up

# %% [markdown]
# Large object that are no longer required can hog a lot of memory, similarly, objects with misspelled names are not supposed to linger.  `xdel` lets you clean up pretty thoroughly.

# %%
xx = np.arange(500.0)

# %%
# %whos

# %%
# %xdel xx

# %%
# %whos

# %% [markdown]
# ## Temporary storage

# %% [markdown]
# You can temporarily store Python objects and retrieve them later.  This can be useful if you need to restart the kernel, but don't want to redo an expensive computations.

# %%
# %store y

# %% [markdown]
# Now delete the object.

# %%
# %xdel y

# %%
# %whos

# %% [markdown]
# And bring it back to life.

# %%
# %store -r y

# %%
# %whos

# %% [markdown]
# ## Timing & benchmarking

# %% [markdown]
# The `%time` and `%timeit` magic commands are very useful for microbenchmarking single Python statements.  If you want to time the execution of an entire cell, so multiple statements, you can use the cell magic `%%time` and `%timeit`.

# %%
# %time z = np.random.uniform(size=100_000_000)

# %%
# %timeit z = np.random.uniform(size=100_000_000)

# %%
# %%timeit
A = np.random.uniform(size=(100, 100))
B = np.random.uniform(size=(100, 100))
A@B

# %% [markdown]
# ## Installing packages

# %% [markdown]
# It happens quite often that you start working on a notebook in a Python virtual environment and you realize you didn't install a Python package that you require.  There are magic commands that will ensure packages are installed in the currect kernel.  Depending on which virtual environments you use, you can use either
# * `%pip` for venv,
# * `%conda` for conda environments, or
# * `%mamba` in case you use mamba.

# %% [markdown]
# ## Displaying files

# %% [markdown]
# Sometimes it can be useful to display the contents of a file in a Jupyter notebook.

# %%
# %cat data.txt

# %%
# %pycat gcd.py

# %% [markdown]
# ## Conclusion

# %% [markdown]
# There are many more magic commands, but these are likely most useful ones.
#
# Remember that magic is only available in notebooks, and hence should *not* be used in production.
