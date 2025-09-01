# Slides

Although quarto does a much better job at slides, it can be useful to use
the basic Jupyter notebook functionality to create simple slides.


## What is it?

1. `slides.ipynb`: simple presentation using Jupyter notebooks, can be
    used with `nbconvert` or RISE.


## How to use it?

You can run the presentation by running the following command in
your terminal:

```bash
$ jupyter nbconvert  slides.ipynb  --to slides  --post serve
```
