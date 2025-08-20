# Marimo interactive notebook
# Author/contact: 23f2000783@ds.study.iitm.ac.in
# How to run:
#   uvx marimo edit analysis.py
# How to export to HTML:
#   uvx marimo export analysis.py
#
# This notebook demonstrates reactive, dependency-driven computation:
# - UI cells define widgets -> downstream data cells depend on them
# - Data cells produce DataFrames -> analysis/plot cells depend on data
# - Markdown is dynamically regenerated when widget state changes

import marimo as mo

app = mo.App()


@app.cell
def _():
    # Imports are exposed for downstream cells.
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    rng = np.random.default_rng(0)
    return np, pd, plt, rng


@app.cell
def _(mo=mo):
    # --- UI WIDGETS (source of truth) ---
    # These widgets drive the entire notebook reactively.
    # Downstream cells *depend* on slider values and will recompute when they change.
    n_slider = mo.ui.slider(50, 1000, value=300, label="Number of samples (n)")
    noise_slider = mo.ui.slider(0.0, 5.0, value=1.0, step=0.1, label="Noise standard deviation (σ)")
    return n_slider, noise_slider


@app.cell
def _(np, pd, rng, n_slider, noise_slider):
    # --- DATA GENERATION (depends on: n_slider, noise_slider) ---
    # Data flow:
    #   UI sliders -> (n, sigma) -> synthetic dataset df -> used by analysis/plot cells
    n = int(n_slider.value)
    sigma = float(noise_slider.value)

    x = rng.normal(0, 1, size=n)
    # True relationship: y = 2x + 3 + ε, where ε ~ N(0, σ^2)
    eps = rng.normal(0, sigma, size=n)
    y = 2 * x + 3 + eps

    df = pd.DataFrame({"x": x, "y": y})
    return df, n, sigma


@app.cell
def _(np, df):
    # --- ANALYSIS (depends on: df) ---
    # Compute correlation and OLS line via polyfit (degree 1).
    r = np.corrcoef(df["x"], df["y"])[0, 1]
    slope, intercept = np.polyfit(df["x"], df["y"], deg=1)
    return r, slope, intercept


@app.cell
def _(mo=mo, r=None, slope=None, intercept=None, n=None, sigma=None):
    # --- DYNAMIC MARKDOWN (depends on: r, slope, intercept, n, sigma) ---
    # Any change upstream re-renders this Markdown automatically.
    md = mo.md(
        f"""
### Relationship summary

- Samples: **{n}**
- Noise σ: **{sigma:.2f}**
- Pearson correlation: **{r:.3f}**
- Fitted model: **y = {slope:.3f}·x + {intercept:.3f}**

**As σ increases**, points spread farther from the line, correlation decreases, and the fitted slope/intercept may drift.
"""
    )
    return md


@app.cell
def _(plt, np, df, slope, intercept):
    # --- VISUALIZATION (depends on: df, slope, intercept) ---
    # Scatter plot with fitted regression line.
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(df["x"], df["y"], alpha=0.6)
    xs = np.linspace(df["x"].min(), df["x"].max(), 100)
    ax.plot(xs, slope * xs + intercept, linewidth=2)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("y vs x with fitted line")
    fig.tight_layout()
    return fig


@app.cell
def _(mo=mo, n_slider=None, noise_slider=None, md=None, fig=None):
    # --- LAYOUT (depends on: widgets, dynamic markdown, figure) ---
    # This cell defines the composed UI. Changing any widget triggers a full reactive update.
    ui = mo.vstack(
        [
            mo.hstack([n_slider, noise_slider], justify="start", gap="large"),
            md,
            fig,
        ],
        gap="large",
    )
    ui  # display
    return


if __name__ == "__main__":
    app.run()
