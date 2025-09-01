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
# # Making slides in Jupyter

# %% [markdown]
# [Geert Jan Bex](geertjan.bex@uhasselt.be)

# %% [markdown]
# ## Text elements

# %% [markdown]
# As you would expect, text can be in *italics* or **bold**, and you can use
#
#   1. ordered lists,
#   1. unordered lists, and
#   1. LaTeX
#   1. code fragments

# %% [markdown]
# ## LaTeX formulas

# %% [markdown]
# The distance between two point $p$ and $q$ in two dimensional space is given by $d(p, q) = \sqrt{(p_x - q_x)^2 + (p_y - q_y)^2}$.

# %% [markdown]
# For more complicated formulas, you may want them on a separate line.
# $$
# n! = \prod_{i=1}^n i
# $$

# %% [markdown]
# ## Python code

# %% [markdown]
# Of course, Python code can be embedded as code cells.

# %%
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# %% [markdown]
# Create and array, compute some values, make a plot.

# %%
x = np.linspace(0.0, 1.0, 101)
y = np.sqrt(x)

# %%
_ = plt.plot(x, y)

# %% [markdown]
# ## Conclusions

# %% [markdown]
# * may be useful
# * fairly quick to make
# * results are not particularly beautiful

# %% [markdown]
# But of course, *beauty is in the eye of the beholder.*
