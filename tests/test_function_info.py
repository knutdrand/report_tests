from report_tests.function_info import get_function_info
from tests.fixtures import example_function


def test_get_function_info():
    info = get_function_info(example_function)
    assert info.title=="example_function"
    assert info.description=="This is an example function."
    assert info.code=="def example_function():\n    '''This is an example function.'''\n    return 1\n"
