# Bash notebooks

It is easy to install an Bash kernel so that you can run Bash notebooks in
Jupyter Lab.


## What is it?

1. `bash_notebook.ipynb`: an example Bash notebook that you can run in Jupyter Lab.
1. `bash_notebook.py`: paired Python sciprt.


## How to install the Bash kernel?

The most convenient way is to install all requirements in a conda environment.

### All-in-one conda environment

```bash
$ conda create  -n bash_notebooks  -c conda-forge  python=3.13 \
      jupyterlab \
      bash_kernel
```

Then activate the environment:

```bash
$ conda activate bash_notebooks
$ python  -m bash_kernel.install  --sys-prefix
```

Finally, run Jupyter Lab:

```bash
$ jupyter lab
```
