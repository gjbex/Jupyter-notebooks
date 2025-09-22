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
# It is good practice to define functions and classes that you intend in modules, rather than directly in a Jupyter notebook.  However, given that the module may change to add features or fix bugs, there would have to be a convenient way to reload it.  This can be accomplished using the `autoreload` extension.
#
# First, load the extension.

# %%
# %load_ext autoreload

# %% [markdown]
# Next, activate the extension, modules will be reloaded before code is executed.

# %%
# %autoreload 2

# %% [markdown]
# Import a module that you are "developing".

# %%
import messages

# %% [markdown]
# This is its current content.

# %%
# %pycat messages.py

# %% [markdown]
# Of course, you can call the function `say_hello`.

# %%
messages.say_hello('gjb')

# %%
help(messages.say_hello)

# %% [markdown]
# Add the following documentation to the `say_hello` function:
# ```
# '''Say hello to someone.
#
# Parameters
# ----------
# name: str
#     name of person to say hello to
# '''
# ```

# %%
help(messages.say_hello)

# %% [markdown]
# Add a new function to the module:
# ```
# def say_bye(name: str) -> None:
#     '''Say bye to someone.
#
#     Parameters
#     ----------
#     name: str
#         name of person to say bye to
#     '''
#     print(f'hello {name}!')
# ```

# %%
messages.say_bye('world')

# %% [markdown]
# Oops, copy/pasting code is a bad idea, fix the message, and run again.

# %%
messages.say_bye('world')

# %% [markdown]
# The `autoreload` extension makes it very easy to mix notebook and module use.

# %% [markdown]
# Sometimes it can be useful for performance reasons not to automatically reload modules.  In that case, you can use
# ```
# %autoreload 1
# ```
# and import the modules that should be reloaded using
# ```
# %aimport messages
# ```
