import plotly.express as px
from plotly.graph_objs import Figure
from matplotlib.figure import Figure as pltFigure

def get_function_output(function):
    result = function()
    if isinstance(result, Figure):
        filename = f"{function.__name__}.png"
        result.write_image(filename)
        return filename
    if isinstance(result, pltFigure):
        filename = f"{function.__name__}.png"
        result.savefig(filename)
        return filename
