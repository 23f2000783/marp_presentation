import marimo as mo

# Email for verification: 23f2000783@ds.study.iitm.ac.in

# --- Cell 1: Interactive Widget ---
# This cell creates an interactive slider. Its value can be used by other cells.
num_points = mo.ui.slider(start=10, stop=100, step=5, value=25, label="Select a value:")


# --- Cell 2: Data Generation (Dependent on Cell 1) ---
# This cell's output depends on the `num_points` slider from Cell 1.
# If you move the slider, this cell will automatically re-run.
data_list = [i * 2 for i in range(num_points.value)]


# --- Cell 3: Dynamic Markdown Output (Dependent on Cell 1) ---
# This markdown text is also reactive and changes based on the slider's value.
mo.md(f"""
    The slider is currently set to **{num_points.value}**.
    
    A list of {num_points.value} numbers has been generated.
""")


# --- Cell 4: Displaying Data (Dependent on Cell 2) ---
# This cell depends on the `data_list` variable created in Cell 2.
mo.md(f"**Generated Data:** `{data_list}`")