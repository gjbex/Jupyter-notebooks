# R notebooks

It is easy to install an R kernel so that you can run R notebooks in Jupyter Lab.


## What is it?

1. `r_notebook.ipynb`: an example R notebook that you can run in Jupyter Lab.
1. `r_notebook.py`: paired Python sciprt.


## How to install the R kernel?

The most convenient way is to install all requirements in a conda environment.

### All-in-one conda environment

```bash
$ conda create  -n r_notebooks  -c conda-forge  python=3.13 \
      jupyterlab \
      r-base r-ggplot2 \
      r-irkernel
```

You can install R package, e.g., `ggplot2`, by adding it to the above command,
or install them later in an R session, e.g., by running
`install.packages("ggplot2")`.

Then activate the environment:

```bash
$ conda activate r_notebooks
```

Finally, run Jupyter Lab:

```bash
$ jupyter lab
```


### Using your existing R installation

Make sure Jupyter Lab is installed in a conda environment, and that the
environment is activated.

Then install the R kernel by running the following command in an R session:

```R
> install.packages('IRkernel')
> IRkernel::installspec(user = TRUE)
```

Now you can run Jupyter Lab:

```bash 
$ jupyter lab
```
