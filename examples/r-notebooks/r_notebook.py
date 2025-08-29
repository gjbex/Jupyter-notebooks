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
#     display_name: R
#     language: R
#     name: ir
#   language_info:
#     codemirror_mode: r
#     file_extension: .r
#     mimetype: text/x-r-source
#     name: R
#     pygments_lexer: r
#     version: 4.4.3
# ---

# %% [markdown]
# # R notebooks

# %% [markdown]
# The default kernel for Jupyter notebooks is Python, however, it is also possbile to run an R kernel.

# %% [markdown]
# ## Demo

# %% [markdown]
# Create a vector of $x$-values, and compute the $y$-values.

# %%
x <- seq(0.0, 1.0, length=101)

# %%
y <- sqrt(x)

# %% [markdown]
# Load the `ggplot2` library.

# %%
library(ggplot2)

# %% [markdown]
# Create a plot of $y$ versus $x$.

# %%
ggplot() + geom_point(aes(x=x, y=y))

# %% [markdown]
# ## Installation

# %% [markdown]
# Installation in a conda environment is straightforward and self-contained.
# ```
# $ conda create  -n r_notebooks  -c conda-forge  python=3.13  jupyterlab r-base r-irkernel
# ```
#
# When the environment is created, activate it, and start Jupyter lab.
# ```
# $ conda activate r_notebooks
# $ jupyter lab
# ```
