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
# ## $\LaTeX$ macros

# %% [markdown]
# You can define your own $\LaTeX$ macros using `\newcommand` as you would in an ordinary $\LaTeX$ file.  If you do that near the top of your document, these macros can be used throughout the notebook.  For this to work, you need to evaluate the cell (this one) containing these macro definitions.
# $$
#   \newcommand{\RR}{\mathbb{R}}
#   \newcommand{\vect}[1]{\boldsymbol{#1}}
#   \newcommand{\argmax}{\mathop{\mathrm{arg\,max}}}
# $$
# In this cell, `\RR` is defined to denote the set of real numbers, `\vect` to typeset a vector in bold, and the mathematical operator `\argmax` that can be used in blocks as well as inline.

# %% [markdown]
# Now in a text, we can use $\RR$ to denote the set of real numbers.  Also $\argmax_i v_i$ works inline and in a block.
# $$
#   \argmax_{i} v_i
# $$
# A vector $\vect{v}$ is also properly rendered.
