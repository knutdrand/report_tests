from plotly import express as px
import matplotlib.pyplot as plt

def example_function():
    '''This is an example function.'''
    return 1

def example_function2():
    '''
    This is an example function.'''
    return 1

def example_function3():
    """
    This is an example function."""
    return 1

def example_function4():
    """
    This is an example function.
    """
    return 1


def plotting_function():
    '''Plots a simple line'''
    return px.line(x=[1, 2, 3], y=[4, 5, 6])


def plt_function():
    '''Plots a simple line'''
    plt.plot([1, 2, 3], [4, 5, 6])
    return plt.gcf()
