# Paired notebooks

This directory contains configuration files for setting up paired Jupyter
notebooks. Jupyter notebooks are paired with MarkDown files.  These files are
automatically synced using the `jupytext` tool.  This is run automatically as a
pre-commit hook.

There are two versions of the pre-commit hook configuration files.  One is for
notebooks/repositories that contain training materials.  It is convenient that
the output cells are included in the notebooks so that learners can see the
results without having to run the cells.  The other configuration file is for
other notebooks/repositories.  In this case, the output cells are not included
in the notebooks.  This minimizes the size of the notebooks and avoids churn.


## What is it?

1. `paired_notebooks.ipynb`: an example Jupyter notebook.
1. `paired_notebooks.md`: the MarkDown file paired with the example Jupyter
   notebook.
1. example_jupitext.toml: configuration file for `jupytext`, to use it in a
   repository, copy this file to `.jupytext.toml` at the top level of the
   repository, or to a specific directory.
1. `pre-commit-config.yaml`: configuration file for `pre-commit` to set up the
   pre-commit hook to run `jupytext` automatically before each commit.  This
   configuration file is for notebooks/repositories not intended as training
   material and will remove output cells from the notebooks.
1. `contributing.md`: instructions for contributing to a repository that has
   paired notebooks.  You can add this MarkDown snippet to your
   `CONTRIBUTING.md` file.
1. `pre-commit-config-training.yaml`: configuration file for `pre-commit` to
   set up the pre-commit hook to run `jupytext` automatically before each
   commit.  This configuration file is for notebooks/repositories intended as
   training material and will keep output cells in the notebooks.
1. `contributing_training.md`: instructions for contributing to a repository
   that has paired notebooks intended as training material.  You can add this
   MarkDown snippet to your `CONTRIBUTING.md` file.


## How to use it?

The `contributing.md` or `contributing_training.md` file contains the
instructions on how to initialize your repository to use paired notebooks.

In summary, you need to:
1. Install `jupytext`, `pre-commit`, `nbstripout`, and `nbdime`: ```bash conda
   install jupytext pre-commit nbstripout nbdime ```
1. Copy `example_jupytext.toml` to `.jupytext.toml` at the top level of your
   repository or to a specific directory.
1. Copy `pre-commit-config.yaml` or `pre-commit-config-training.yaml` to
   `.pre-commit-config.yaml` at the top level of your repository.
1. Run `pre-commit install` to set up the Git hooks.
1. Run `nbdime config-git --enable` to set up notebook-aware git diffs.

From now on, whenever you `git commit`, the hooks will:
   - sync `.ipynb` ↔ paired `.md` (via Jupytext),
   - strip outputs and noisy metadata from notebooks (via nbstripout) if you
     used `pre-commit-config.yaml`,
   - ensure git diffs are notebook-aware (via nbdime).
