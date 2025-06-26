import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add a title for the page
ui.page_opts(title="PyShiny App with plot", fillable=True)

# Add a string id, label, and integers representing the min, max, and initial values
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 150, 17)


@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.selected_number_of_bins(), density=True)
