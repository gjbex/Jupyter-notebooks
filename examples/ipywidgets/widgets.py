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
# # Interactive notebooks

# %% [markdown]
# `ipywidgets` provides the Python bindings for interactive elements in Jupyter notebooks.  Bindings for other language to use with non-Python kernels are available as well.

# %%
from ipywidgets import interact, interact_manual
import matplotlib.pyplot as plt
import numpy as np
import warnings


# %% [markdown]
# ## Fast compute

# %% [markdown]
# ### Example 1: sigmoid function

# %% [markdown]
# Define a function that will plot $\tanh(\beta x)$ for $x \in [-5, 5]$ and $\beta > 0$ a parameter value.

# %%
def plot_tanh(beta):
    x = np.linspace(-5.0, 5.0, 101)
    y = np.tanh(beta*x)
    _ = plt.plot(x, y)


# %% [markdown]
# Now this function can be run for various values of `beta`, e.g.,

# %%
plot_tanh(0.6)

# %%
plot_tanh(4.0)


# %% [markdown]
# However, it would be much more interesting if the value of `beta` could be modified interactively, the plot modified on the fly.  A simple function decorated with accomplish this easily.

# %%
@interact(beta=(0.2, 5.0, 0.2))
def plot_tanh(beta):
    x = np.linspace(-5.0, 5.0, 101)
    y = np.tanh(beta*x)
    _ = plt.plot(x, y)


# %% [markdown]
# A plot can be parameterized by multiple values, either numerical or categorical.

# %% [markdown]
# ### Example 2: viral load

# %% [markdown]
# A model for the viral load is given by
# $$
# V(t) = A e^{-\alpha t} + B e^{-\beta t}
# $$
# This expression can be rewritten as
# $$
# V(t) = A e^{-\alpha t} (1 + \frac{B}{A} e^{-(\beta - \alpha)t}
# $$
# In order to study this function qualitatively, we can set $A = 1$ and $\alpha = 1$.  We know that $-1 \leq B \leq 0$, $1 \leq \beta$, two independent quantities.

# %%
@interact(B=(-1.0, 0.0, 0.05), beta=(1.0, 8.0, 0.1))
def viral_load_plot(B, beta):
    t = np.linspace(0.0, 7.0, 101)
    v = np.exp(-t)*(1.0 + B*np.exp(-(beta - 1.0)*t))
    _ = plt.plot(t, v)
    _ = plt.ylim(0.0, 1.0)
    _ = plt.xlabel('$t$')
    _ = plt.ylabel('$V(t)$')


# %% [markdown]
# ## Slow compute

# %% [markdown]
# ### Example: Julia set

# %% [markdown]
# Define a function that computes the number of iterations of $z = z^2 + c$ such that $|z| < 2$ in the complex plane.

# %%
def compute_fractal(c_re, c_im):
    c = complex(c_re, c_im)
    max_iters = 255
    nr_points = 1000
    max_val = 1.8
    max_norm = 2.0
    x = np.linspace(-max_val, max_val, nr_points)
    y = np.linspace(-max_val, max_val, nr_points)
    X, Y = np.meshgrid(x, y)
    Z = X + Y*1j
    iterations = np.zeros(Z.shape, dtype=np.uint8)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        for _ in range(max_iters):
            Z = Z**2 + c
            iterations[np.abs(Z) < max_norm] += 1
    return iterations
        


# %% [markdown]
# Define a function to plot the result of that function as a heatmap.

# %%
def plot_fractal(c_re=-0.62, c_im=0.52):
    ns = compute_fractal(c_re, c_im).astype(np.float32)
    _, axes = plt.subplots()
    axes.imshow(ns/np.max(ns), cmap='RdBu')
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)


# %% [markdown]
# You can call this function for various values of the real and imaginary part of $c$.

# %%
plot_fractal(-0.622772, 0.52193j)

# %%
plot_fractal(-0.78, 0.86j)

# %% [markdown]
# However, the function takes a while to evaluate.

# %%
# %timeit compute_fractal(-0.6, 0.4)

# %% [markdown]
# On average, it takes more than half a second to complete the computation, so making this interactive and just touching the sliders would result in jaggy output (at least).  Hence `interact_manual` is more appropriate, since the computation is only initiated when the `Run interact` button is pressed.

# %%
_ = interact_manual(plot_fractal, c_re=(-1.0, 1.0, 0.01), c_im=(-1.0, 1.0, 0.01))

# %% [markdown]
# ## Linked plots

# %% [markdown]
# Altair is an interesting visualization library that is mainly intended for information visualization, but can handle a number of scientific visualization tasks as well.  Here, two plots that are linked will be illustrated.

# %%
import altair as alt
alt.renderers.enable('jupyterlab')
import pandas as pd
from scipy.integrate import ode


# %% [markdown]
# ### Example: oscillator

# %% [markdown]
# The set of ordinary differential equations describing an oscillator with length $l = g$ is given by
#
# $$
#     \begin{array}{rcl}
#         \frac{d\theta}{dt} & = & \omega \\
#         \frac{d\omega}{dt} & = & -\theta - q\omega + F_D \sin(\Omega_D t)
#     \end{array}
# $$
#
# These equations can be solved using `ode` in the `scipy.integrate` module.  We have to define a function that computes the right-hand side of the equations above.

# %%
def func(t, y, q=0.0, F_D=0.0, Omega_D=0.0, linear=True):
    theta, omega = y[0], y[1]
    if linear:
        return [
            omega,
            -theta - q*omega + F_D*np.sin(Omega_D*t)
        ]
    else:
        return [
            omega,
            -np.sin(theta) - q*omega + F_D*np.sin(Omega_D*t)
        ]


# %% [markdown]
# We also need to provide the Jacobian of the right-hand sides.

# %%
def jac(t, y, q=0.0, F_D=0.0, Omega_D=0.0, linear=True):
    theta, omega = y[0], y[1]
    if linear:
        [[0.0, 1.0],
         [-1.0, -q]]
    else:
        [[0.0, 1.0],
         [-np.cos(theta), -q]]


# %% [markdown]
# The function below will integrate the equations in the interval $0 \le t \le t_{\rm max}$.

# %%
def solve(t_max=20.0, delta_t = 0.01, q=0.0, F_D=0.0, Omega_D=0.0, linear=True, theta0=0.1):
    t, theta, omega = 0.0, theta0, 0.0
    ts, thetas, omegas = [t], [theta], [omega]
    system = ode(func, jac).set_integrator('dopri5') \
                           .set_f_params(q, F_D, Omega_D, linear) \
                           .set_jac_params(q, F_D, Omega_D, linear) \
                           .set_initial_value((theta, omega), t)
    while system.successful() and system.t <= t_max:
        system.integrate(system.t + delta_t)
        ts.append(system.t)
        thetas.append(system.y[0])
        omegas.append(system.y[1])
    
    return pd.DataFrame({'t': ts, 'theta': thetas, 'omega': omegas})


# %% [markdown]
# The function below will solve and plot the solution to the differential equations.

# %%
def solve_plot(t_max=20.0, delta_t = 0.01, q=0.0, F_D=0.0, Omega_D=0.0, linear=True, theta0=0.1):
    data = solve(t_max, delta_t, q, F_D, Omega_D, linear, theta0)
    brush = alt.selection_interval(resolve='global')
    chart = alt.Chart(data).mark_point(size=1).encode(
        color=alt.condition(brush, alt.value("black"), alt.value("lightgray")),
        opacity=alt.condition(brush, alt.value(1.0), alt.value(0.2)),
    ).add_params(
        brush
    )
    return chart.encode(x='t:Q', y='theta:Q') | chart.encode(x='theta:Q', y='omega:Q')


# %%
solve_plot(t_max=40.0, q=0.2, F_D=0.1, Omega_D=0.3)

# %% [markdown]
#     This interactive plot can be combined with `ipywidgets` as well.

# %%
_ = interact_manual(solve_plot, t_max=(10.0, 45.0, 0.5), delta_t=(0.001, 0.01, 0.005),
                    q=(0.0, 2.0, 0.1), F_D=(0.0, 2.0, 0.1), Omega_D=(0.0, 2.0*np.pi, 0.1),
                    linear=[False, True], theta0=(0.0, np.pi, 0.05))

# %% [markdown]
# ## Animations

# %% [markdown]
# It is also possible to get animations in a notebook.  These can be displayed using an `HTML` element in the notebook, and created using `matplotslib`'s `animation` module.  This can be very useful for teaching purposes or exploration.

# %% [markdown]
# The example below builds on the previous oscillator example.

# %%
from IPython.display import HTML
import matplotlib.animation


# %%
def solve_animate(t_max=20.0, delta_t = 0.01, q=0.0, F_D=0.0, Omega_D=0.0, linear=True, theta0=0.1):
    data = solve(t_max, delta_t, q, F_D, Omega_D, linear, theta0)
    theta_min, theta_max = data[['theta']].values.min(), data[['theta']].values.max()
    omega_min, omega_max = data[['omega']].values.min(), data[['omega']].values.max()
    figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
    axes[0].axis([0.0, t_max, theta_min, theta_max])
    axes[0].set_xlabel('$t$')
    axes[0].set_ylabel(r'$\theta(t)$')
    axes[1].axis([theta_min, theta_max, omega_min, omega_max])
    axes[1].set_xlabel(r'$\theta(t)$')
    axes[1].set_ylabel(r'$\omega(t)$')
    theta_plot, = axes[0].plot([], [])
    phase_plot, = axes[1].plot([], [])
    figure.tight_layout()
    def animate(i):
        theta_plot.set_data(data[['t']][:i].values, data[['theta']][:i].values)
        phase_plot.set_data(data[['theta']][:i], data[['omega']][:i])
    animation = matplotlib.animation.FuncAnimation(figure, animate, frames=len(data))
    plt.close(figure) 
    return HTML(animation.to_jshtml())


# %%
solve_animate(t_max=40.0, delta_t=0.3, q=0.2, F_D=0.1, Omega_D=0.3)

# %% [markdown]
# ## Exploring pandas `DataFrames`

# %% [markdown]
# Although pandas by itself is very useful for data exploration, sometimes an additional level of interactivity may be convenient.  `ipydatagrid` can be used for an "Excel-like" experience in a Jupyter notebook.

# %%
import ipydatagrid
import pandas as pd
import random

# %% [markdown]
# We create a dataframe with two columns, the first has categorical data, the second quantitative data.

# %%
nr_items = 100
nr_values = 15
values = {f'value_{v_id}': [random.random() for _ in range(nr_items)] for v_id in range(1, nr_values + 1)}
data = pd.DataFrame({
    'category': random.choices(('A', 'B', 'C'), k=nr_items),
    **values
})

# %% [markdown]
# The table below can be sorted by any column, or filtered by any column, e.g., filter `category` to show only category `"A"`, `value` to only show positive numbers.

# %%
data_grid = ipydatagrid.DataGrid(data, editable=True)
data_grid

# %%
data_grid.data[['category', 'value_1']]

# %% [markdown]
# The filtered/edited data can be saved into a new dataframe for further processing.

# %%
filtered_data = data_grid.get_visible_data()

# %%
filtered_data

# %% [markdown]
# `ipydatagrid` offers many options for sophisticated data analysis and representation.
