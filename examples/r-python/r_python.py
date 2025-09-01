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
# # Using Python & R in the same notebook

# %% [markdown]
# To run this notebook, an implementation of R should be installed in your environment, as well as the `rpy2` package that "translates" between Python and R data types.

# %% [markdown]
# The easiest way to install the requirements is to use conda, e.g.,
# ~~~bash
# $ conda create  -n rpy  -c conda-forge  rpy2 numpy matplotlib pandas r-base r-ggplot jupyterlab
# ~~~

# %% [markdown]
# Import numpy for numerical arrays in Python, and load the `rpy2` iPython extension.

# %%
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import pandas as pd
# %load_ext rpy2.ipython

# %% [markdown]
# ## Translating variables between Python and R

# %% [markdown]
# Define a vector in R, and assign it to the variable `values`, which is exported to Python (`-o` option).

# %% magic_args="-o values" language="R"
# values <- c(3, 7, 5)

# %% [markdown]
# `values` is now also a Python variable, translated by `rpy2` to a numpy array.

# %%
type(values)

# %% [markdown]
# Now any Python function or numpy method that works on numpy arrays can be called.

# %%
sum(values)

# %% [markdown]
# We can define a numpy array, and use that in R as if it were a vector.

# %%
p_values = np.array([3, 7, 9], dtype=np.float64)

# %% magic_args="-i p_values -o my_sum" language="R"
# cat('R type:', typeof(p_values))
# my_sum <- sum(p_values)

# %% [markdown]
# Although the result is semantically a number, it is returned as a `FloatVector` as is typical in R.

# %%
type(my_sum)

# %%
print(my_sum[0])

# %%
type(my_sum[0])

# %% [markdown]
# As an alternative to the cell magic `%%R -i` and `%%R -o`, you can also use the `%Rpush` and `%Rpull` magic.  This simply "transfers" data to and from R, respectively.

# %% [markdown]
# Create a numpy array, and push it to R.

# %%
x = np.linspace(0.0, 1.0, 101)

# %%
# %Rpush x

# %% [markdown]
# Do some computations in R, e.g., computing the square root of `x`.

# %% language="R"
# y = sqrt(x)

# %% [markdown]
# Get the resulting `y` values back into Python.

# %%
# %Rpull y

# %% [markdown]
# Plot `y` versus `x` using matplotlib.

# %%
plt.plot(x, y);

# %% [markdown]
# ## Using R libraries

# %% [markdown]
# Load the required R library `ggplot2` using `require`.

# %%
# %R require(ggplot2)

# %% [markdown]
# Create a data with four columns. The first, `letter`, is categorical with values `a`, `b`, `c`.  The three other columns, `X`, `Y` and `Z` have numerical values between 1 and 9, 0 and 13, and 1 and 3 respectively.

# %%
df = pd.DataFrame({
        'Letter': ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
        'X': [4, 3, 5, 2, 1, 7, 7, 5, 9],
        'Y': [0, 4, 3, 6, 7, 10, 11, 9, 13],
        'Z': [1, 2, 3, 1, 2, 3, 1, 2, 3]
    })

# %% [markdown]
# Create a plot using `ggplot` that uses the data frame as data, creates a geometric point plot using `x` and `Y` as axes (`aes`), the categorical data as color, and `Z` as size.

# %% magic_args="-i df" language="R"
# ggplot(data = df) + geom_point(aes(x = X, y= Y, color = Letter, size = Z))

# %% [markdown]
# It is clear that using line and cell magic helps to integrate Python and R in one and the same notebook, allowing for a mixed computation, converting values back and forth between the languages.
