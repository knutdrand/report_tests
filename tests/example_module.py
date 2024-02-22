'''
Example text
'''
from matplotlib import pyplot as plt
from report_tests import show

def test_example():
    assert True


def test_example2():
    '''With docstring'''
    plt.plot([1, 2, 3], [4, 5, 6])
    return show(plt.gcf())
