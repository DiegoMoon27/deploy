import numpy as np
import plotly.express as px


def get_random_scatter():

    x_values = np.random.randint(-50,50,100)
    y_values = np.random.randint(-50,50,100)

    return px.scatter(x = x_values, y = y_values)

