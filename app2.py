import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Page title and layout
ui.page_opts(title="PyShiny App with plot", fillable=True)

# Sidebar inputs
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 5, 150, 17)
    ui.input_select("hist_color", "Histogram Color", 
                    {"blue": "Blue", "green": "Green", "red": "Red", "purple": "Purple"}, 
                    selected="blue")

@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)

    plt.figure(figsize=(8, 5))
    
    # Add edge color to separate bars
    plt.hist(x, bins=input.selected_number_of_bins(), density=True, 
             color=input.hist_color(), edgecolor='black', alpha=0.7)
    
    # Add labels and a grid for clarity
    plt.title("Histogram of Random Data")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.grid(True)
    plt.tight_layout()
