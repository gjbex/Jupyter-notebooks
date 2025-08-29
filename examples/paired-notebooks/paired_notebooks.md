---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    formats: ipynb,md
    notebook_metadata_filter: kernelspec,language_info
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.7.2
---

# Paired notebooks

```python
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
```

```python
x = np.linspace(0.1, 3.0, 101)
y = np.log(x)
```

```python
_ = plt.plot(x, y)
```

```python
y = np.sqrt(x)
```

```python
_ = plt.plot(x, y)
_ = plt.xlabel('x')
_ = plt.ylabel('y')
```
