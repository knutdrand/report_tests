from report_tests.function_output import get_function_output
from tests.fixtures import plotting_function, plt_function


def test_get_function_output():
    filename = get_function_output(plotting_function)
    assert filename.endswith("plotting_function.png")


def test_get_function_output_plt():
    filename = get_function_output(plt_function)
    assert filename.endswith("plt_function.png")
