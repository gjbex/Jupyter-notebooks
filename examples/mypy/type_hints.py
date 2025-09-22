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
# You can enable Python's type hints checking in Jupyter Lab by installing the `nb_mypy` extension using `pip install nb_mypy`.  Once installed, you load the extension in the session you want typechecking in.

# %%
# %load_ext nb_mypy

# %% [markdown]
# To activate type checking, turn it on.

# %%
# %nb_mypy On

# %% [markdown]
# The following function expects a `str` parameter.

# %%
def say_hello(name: str) -> None:
    print(f'hello {name}!')


# %% [markdown]
# When calling it with a string, e.g., `'gjb'`, everything is well.

# %%
say_hello('gjb')

# %% [markdown]
# On the other hand, if you can it with, e.g., an `int`, an error message is printed, but note that the code is executed, as you would expect.

# %%
say_hello(5)

# %%
