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
# # Mixing Bash & Python

# %% [markdown]
# Interacting with the host operating system can be done directly through notebook magic, rather than using, e.g., the subprocess Python module.

# %% [markdown]
# Arbitrary shell commands can be executed, e.g., grep the password file.

# %%
# ! grep gjb /etc/passwd

# %% [markdown]
# However, the result can also be captured into a Python variable, e.g., the list of files in the currect directory can be acquired using the `!` magic.

# %%
# files = !ls

# %%
files

# %% [markdown]
# The Bash statement can contain variables defined in the notebook.

# %%
directory = 'ipywidgets'

# %%
# ! ls ./{directory}

# %% [markdown]
# Using the `%env` magic, it is possible to set environment variables that will be defined in subprocesses, for instance, set `MAX_VAL` to 12.

# %%
# %env MAX_VAL 12

# %% [markdown]
# This environment can now be used in a somewhat lengthier Bash script executed using the `%%script` magic.  The standard output and standard error can be captured in Python variables if desired.  For instance, echo all number between 5 and `$MAX_VAL`.

# %% magic_args="bash --out numbers" language="script"
# for i in $(seq 5 ${MAX_VAL})
# do
#     echo $i
# done

# %% [markdown]
# The value in `numbers` is a string, if the output had multiple lines, they are separated by `\n`.

# %%
numbers

# %% [markdown]
# You can use this variable just as expected, e.g., split the lines, and convert to integer values.

# %%
sequence = list(map(int, numbers.split()))
sequence

# %% [markdown]
# ## When to use magic

# %% [markdown]
# Although you can use this to install Python packages using `pip`, `conda` or `mamba`, it is better to use the corresponding magic commands `%pip`, `%conda` and `%mamba`.  This ensures the new packages get installed into the current kernel.

# %% [markdown]
# ## When to use `multiprocessing`

# %% [markdown]
# While useful for quick hacks in Jupyter notebooks, this kind of interaction with the shell is not really your best option since it is only available in Jupyter Lab or iPython.
#
# For robust scripting, either `sh` (third-party) or the `multiprossing` module (standard library) is a much more efficient and versatile approach.
