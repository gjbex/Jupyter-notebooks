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
#     display_name: Bash
#     language: bash
#     name: bash
#   language_info:
#     codemirror_mode: shell
#     file_extension: .sh
#     mimetype: text/x-sh
#     name: bash
# ---

# %% [markdown]
# # Bash notebooks

# %% [markdown]
# Jupyter notebooks can also use a Bash kernel.

# %% [markdown]
# Compute the squares of integers from 1 to 10.

# %%
for i in $(seq 1 10)
do
    echo $i, $(( $i**2 ))
done

# %% [markdown]
# Get the file size of all Jupyter notebooks in the current working directory

# %%
ls -lh *.ipynb | cut -d ' ' -f 5- | sed 's/^ \+//' | cut -d ' ' -f 1

# %% [markdown]
# Check the above result.

# %%
ls -lh *.ipynb
