# Contributing Guidelines

## Notebook policy
- We version-control Jupyter notebooks (`.ipynb`) **without outputs** for minimal Git churn.
- Each notebook is paired with a clean text representation (`.py` or `.md`) using [Jupytext].
- Outputs and execution counts are stripped automatically when you commit.
- Notebook diffs and merges are handled by [nbdime] for better readability.

## First-time setup
1. Clone the repo and install the dev tools:
    
    ```bash
    pip install pre-commit jupytext nbstripout nbdime
    ```

2. Enable the Git hooks:
    
    ```bash
    pre-commit install
    ```

3. Enable notebook-aware diffs:
    
    ```bash
    nbdime config-git --enable
    ```

Now, whenever you `git commit`, the hooks will:
- sync `.ipynb` ↔ paired `.py`/`.md` (via Jupytext),
- strip outputs and noisy metadata from notebooks (via nbstripout),
- ensure diffs are notebook-aware (via nbdime).

## Day-to-day workflow
- **Edit notebooks** in JupyterLab, VS Code, or your preferred frontend.
- **Commit both** `notebook.ipynb` and its paired text file.
- **Do not** manually edit the paired text unless you know what you’re doing; always save from the notebook.
- **Large data/figures**: keep out of Git. Use external storage or DVC.

## Tips
- If you see unexpected churn in diffs, check that you ran `pre-commit install`.
- If you need to *share notebooks with outputs* (e.g. for teaching material), run:
    
    ```bash
    jupyter nbconvert --to notebook --execute notebook.ipynb
    ```
    
    and export the executed `.ipynb` separately (not committed).

---

[Jupytext]: https://jupytext.readthedocs.io/
[nbdime]: https://nbdime.readthedocs.io/
